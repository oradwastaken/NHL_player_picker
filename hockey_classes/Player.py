from dataclasses import dataclass
from hockey_classes.Position import Position
from datetime import date
from typing import Union
import csv


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