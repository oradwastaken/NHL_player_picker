from dataclasses import dataclass
from enum import Enum, auto
from datetime import date
from typing import Optional, Union
from random import sample
import pickle


class Position(Enum):
    C = auto()
    LW = auto()
    RW = auto()
    D = auto()
    G = auto()

    def __str__(self):
        return self.name


@dataclass
class SkaterStats:
    G: int
    A: int
    Blk: int
    Hit: int

    @property
    def Pts(self):
        return self.G + self.A

    def __str__(self):
        return f"G:{self.G} | A:{self.A} | Blk:{self.Blk} | Hit:{self.Hit}"


@dataclass
class GoalieStats:
    W: int
    L: int
    GAA: float
    SVPcT: float
    SO: int

    def __str__(self):
        return f"W:{self.W} | L:{self.L} | GAA:{self.GAA} | SVPcT:{self.SVPcT} | SO:{self.SO}"


@dataclass
class Player:
    name: str
    team: str
    DOB: date
    ELO_rating: float
    position: Position
    GP: int
    stats: Union[SkaterStats, GoalieStats]

    def __str__(self):
        return f'{self.name} ({self.position})'

    def player_info(self):
        return f'{self.name} ({self.position}), Age: {self.age} // {self.GP} GP | {self.stats}'

    @property
    def age(self):
        born = self.DOB
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def set_rating(self, new_rating):
        self.ELO_rating = new_rating


class Rankings:
    ELO_k = 40
    filename = 'rankings.pickle'

    def __init__(self):
        self.player_list = []

    def __str__(self):
        self.player_list.sort(key=lambda player_temp: player_temp.ELO_rating, reverse=True)

        ranking_str = '\nPlayer rankings\n===============\n'
        for i, player in enumerate(self.player_list):
            ranking_str = f'{ranking_str}#{i + 1}: {player} | ELO: {player.ELO_rating:.2f}\n'
        return ranking_str

    def add_player(self, new_player: Player):
        if new_player not in self.player_list:
            self.player_list.append(new_player)

    def write_list_to_file(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.player_list, file)

    def read_list_from_file(self):
        with open(self.filename, 'rb') as file:
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
