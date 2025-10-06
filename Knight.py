import Piece
from Board import BOARD_LENGTH, BOARD_WIDTH

class Knight(Piece):
    def move(self):
        moveset = []
        
        