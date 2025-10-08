import Piece
from Board import BOARD_LENGTH, BOARD_WIDTH

class Rook(Piece):
    def move(self):
        moveset = []
        
        for i in range(BOARD_LENGTH):
            for j in range(BOARD_WIDTH):
                # All spaces in the row and spaces in the column
                if i == self.curr_position[0] or j == self.curr_position[1]:
                    moveset.append( (i, j) )
        
        return moveset