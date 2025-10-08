import Piece
from Board import BOARD_LENGTH, BOARD_WIDTH

class Bishop(Piece):
    def move(self):
        moveset = []
        
        for i in range(BOARD_LENGTH):
            for j in range(BOARD_WIDTH):
                # diagonal movement
                if abs(self.curr_position[0] - i) == abs(self.curr_position[1] - j) and self.curr_position != (i, j):
                    moveset.append( (i, j) )
        
        return moveset