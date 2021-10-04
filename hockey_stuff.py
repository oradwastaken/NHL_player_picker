from dataclasses import dataclass
from enum import Enum, auto
from datetime import date
from typing import Optional, Union
from random import sample


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


@dataclass
class GoalieStats:
    W: int
    L: int
    GAA: float
    SVPcT: float
    SO: int


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
        return f'{self.name} ({self.position}) ELO:{self.ELO_rating:.2f}'

    @property
    def age(self):
        born = self.DOB
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def set_rating(self, new_rating):
        self.ELO_rating = new_rating


class Rankings:
    ELO_k = 40

    def __init__(self):
        self.player_list = []

    def __str__(self):
        self.player_list.sort(key=lambda player_temp: player_temp.ELO_rating)

        ranking_str = ''
        for i, player in enumerate(self.player_list):
            ranking_str = f'{ranking_str}{i + 1}: {player}\n'
        return ranking_str

    def add_player(self, new_player: Player):
        self.player_list.append(new_player)

    def random_matchup(self):
        player1, player2 = sample(self.player_list, 2)
        R1 = 10 ** (player1.ELO_rating / 400)
        R2 = 10 ** (player2.ELO_rating / 400)
        E1 = R1 / (R1 + R2)
        E2 = R2 / (R1 + R2)

        print(f'#1: {player1}')
        print(f'#2: {player2}')
        print(f'#3: TIE!')
        print('Who would you rather have on your team? Player #1 or #2?')
        while (userinput := input('(1/2/3)? ')) not in ['1', '2', '3']:
            print('Please type 1, 2 or 3:')

        if userinput == '1':
            print(f'{player1.name} wins')
            S1, S2 = 1, 0

        if userinput == '2':
            print(f'{player2.name} wins')
            S1, S2 = 1/2, 1/2

        if userinput == '3':
            print(f"It's a tie!")
            S1, S2 = 0, 1

        player1.set_rating(player1.ELO_rating + self.ELO_k * (S1 - E1))
        player2.set_rating(player2.ELO_rating + self.ELO_k * (S2 - E2))

        print("\nNew values:")
        print(player1)
        print(player2)