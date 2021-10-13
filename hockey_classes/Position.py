from enum import Enum, auto


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
