from dataclasses import dataclass
from enum import Enum, auto
from datetime import date
from typing import Union
from random import sample
import pickle
import csv


class Position(Enum):
    C = auto()
    LW = auto()
    RW = auto()
    D = auto()
    G = auto()

    def __str__(self):
        return self.name

    @staticmethod
    def from_string(position_string):
        conversion_table = {'C': Position.C, 'LW': Position.LW, 'RW': Position.RW, 'D': Position.D, 'G': Position.G}
        return conversion_table[position_string]


@dataclass
class SkaterStats:
    GP: int
    G: int
    A: int
    Blk: int
    Hit: int

    @property
    def Pts(self):
        return self.G + self.A

    def __str__(self):
        return f"GP:{self.GP} | G:{self.G} | A:{self.A} | Blk:{self.Blk} | Hit:{self.Hit}"

    def to_list(self):
        return [self.GP, self.G, self.A, self.Blk, self.Hit]


@dataclass
class GoalieStats:
    GP: int
    W: int
    L: int
    GAA: float
    SVPcT: float
    SO: int

    def __str__(self):
        return f"GP:{self.GP} | W:{self.W} | L:{self.L} | GAA:{self.GAA} | SVPcT:{self.SVPcT} | SO:{self.SO}"

    def to_list(self):
        return [self.GP, self.W, self.L, self.GAA, self.SVPcT, self.SO]


@dataclass
class Player:
    name: str
    team: str
    DOB: date
    ELO_rating: float
    position: Position
    stats: Union[SkaterStats, GoalieStats]

    def __str__(self):
        return f'{self.name} ({self.position})'

    def player_info(self):
        return f'{self.name} ({self.position}), Age: {self.age} // {self.stats}'

    def to_list(self):
        return [self.name, self.team, self.DOB, self.ELO_rating, self.position, *self.stats.to_list()]

    @property
    def age(self):
        born = self.DOB
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def set_rating(self, new_rating):
        self.ELO_rating = new_rating

    def to_csv(self, filename):
        with open(filename, 'a') as csvfile:
            playerwriter = csv.writer(csvfile)
            playerwriter.writerow(self.to_list())


class Rankings:
    ELO_k = 40

    def __init__(self):
        self.player_list = []

    def __str__(self):
        self.sort_list()

        ranking_str = '\nPlayer rankings\n===============\n'
        for i, player in enumerate(self.player_list):
            ranking_str = f'{ranking_str}#{i + 1}: {player} | ELO: {player.ELO_rating:.2f}\n'
        return ranking_str

    def add_player(self, new_player: Player):
        if new_player not in self.player_list:
            self.player_list.append(new_player)

    def sort_list(self):
        self.player_list.sort(key=lambda player_temp: player_temp.ELO_rating, reverse=True)

    def to_csv(self, filename):
        self.sort_list()
        with open(filename, 'wb') as file:
            for player in self.player_list:
                player.to_csv(filename)

    def from_csv(self, filename):
        with open(filename, 'r') as csvfile:
            playerreader = csv.reader(csvfile)
            for row in playerreader:
                player_position = Position.from_string(row[4])
                if player_position == Position.G:
                    new_player = Player(row[0], row[1], date(1984, 11, 28), float(row[3]), player_position,
                                        GoalieStats(GP=int(row[5]), W=int(row[6]), L=int(row[7]), GAA=float(row[8]),
                                                    SVPcT=float(row[9]), SO=int(row[10])))
                else:
                    new_player = Player(row[0], row[1], date(1984, 11, 28), float(row[3]), player_position,
                                        SkaterStats(GP=int(row[5]), G=int(row[6]), A=int(row[7]), Blk=int(row[8]),
                                                    Hit=int(row[9])))
                self.player_list.append(new_player)

    def to_pickle(self, filename):
        self.sort_list()
        with open(filename, 'wb') as file:
            pickle.dump(self.player_list, file, protocol=pickle.HIGHEST_PROTOCOL)

    def from_pickle(self, filename):
        with open(filename, 'rb') as file:
            self.player_list = pickle.load(file)

    def update(self):
        pass

    def random_matchup(self):
        player1, player2 = sample(self.player_list, 2)
        R1 = 10 ** (player1.ELO_rating / 400)
        R2 = 10 ** (player2.ELO_rating / 400)
        E1 = R1 / (R1 + R2)
        E2 = R2 / (R1 + R2)

        print('Who would you rather have on your team?')
        print(f'(1) {player1.player_info()}')
        print(f'(2) {player2.player_info()}')
        print(f"(3) I can't decide!")
        print(f"(4) I don't know...")
        while (userinput := input('(1/2/3/4)? ')) not in ['1', '2', '3', '4']:
            print('Please type 1, 2, 3 or 4:')

        if userinput == '4':
            print(f"OK I'll do nothing!")
            return

        if userinput == '1':
            S1, S2 = 1, 0

        if userinput == '2':
            S1, S2 = 0, 1

        if userinput == '3':
            S1, S2 = 1 / 2, 1 / 2

        player1.set_rating(player1.ELO_rating + self.ELO_k * (S1 - E1))
        player2.set_rating(player2.ELO_rating + self.ELO_k * (S2 - E2))
