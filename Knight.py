import Piece
from Board import BOARD_LENGTH, BOARD_WIDTH

class Knight(Piece):
    def move(self):
        moveset = []
        row, col = self.curr_position

        for i in range(BOARD_LENGTH):
            for j in range(BOARD_WIDTH):
                # One direction 2 spaces, 1 space either left or right of that direction
                if (abs(row - i) == 2 and abs(col - j) == 1) or (abs(row - i) == 1 and abs(col - j) == 2):
                    moveset.append( (i, j) )
        
        return moveset
        
        