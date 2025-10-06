from Pawn import Pawn
from Bishop import Bishop
from Knight import Knight
from Rook import Rook
from Queen import Queen
from King import King

class Board():
    def __init__(self):
        self.array = [ [Rook(), Knight(), Bishop(), Queen(), King(), Bishop(), Knight(), Rook()],
                       [Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn()],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn()],
                       [Rook(), Knight(), Bishop(), Queen(), King(), Bishop(), Knight(), Rook()] ]
        