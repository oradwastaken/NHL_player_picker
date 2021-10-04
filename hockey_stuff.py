from dataclasses import dataclass
from enum import Enum, auto
from datetime import date
from typing import Optional, Union


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
        return f'{self.name} ({self.position}) ELO:{self.ELO_rating}'

    @property
    def age(self):
        born = self.DOB
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def set_rating(self, new_rating):
        self.ELO_rating = new_rating


@dataclass()
class Rankings:
    def __init__(self):
        self.player_list = []

    def __str__(self):
        self.player_list.sort(key=lambda player: player.ELO_rating)

        ranking_str = ''
        for i, player in enumerate(self.player_list):
            ranking_str = f'{ranking_str}{i + 1}: {player}\n'
        return ranking_str

    def add_player(self, new_player: Player):
        self.player_list.append(new_player)

    def matchup(self, player1, player2):
        print('Who would you rather have on your team? Player #1 or #2?')
        print(f'#1: {player1}')
        print(f'#2: {player2}')
        while (userinput := int(input('[1/2]?'))) not in [1, 2]:
            print('Please type 1 or 2')
        if userinput == 1:
            print(f'{player1.name} wins')
        if userinput == 2:
            print(f'{player2.name} wins')
