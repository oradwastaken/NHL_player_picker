from dataclasses import dataclass
from enum import Enum, auto
from datetime import date


class Position(Enum):
    C = auto()
    LW = auto()
    RW = auto()
    D = auto()
    G = auto()

    def __str__(self):
        return self.name



@dataclass
class Player:
    name: str
    team: str
    DOB: date
    ELO_rating: float
    position: Position

    def __str__(self):
        return f'{self.name} ({self.position})'

    @property
    def age(self):
        born = self.DOB
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def win(self, other_player):
        pass


