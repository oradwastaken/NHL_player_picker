from dataclasses import dataclass
from enum import Enum, auto
from datetime import date
from typing import Optional


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
    skater_stats: Optional[SkaterStats] = None
    goalie_stats: Optional[GoalieStats] = None

    def __str__(self):
        return f'{self.name} ({self.position})'

    @property
    def age(self):
        born = self.DOB
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def set_rating(self, new_rating):
        self.ELO_rating = new_rating

    def win_against(self, other_player):
        pass
