import Piece
from Board import BOARD_LENGTH, BOARD_WIDTH

class Knight(Piece):
    def move(self):
        moveset = []

        for i in range(BOARD_LENGTH):
            for j in range(BOARD_WIDTH):
                # One direction 2 spaces, 1 space either left or right of that direction
                if (abs(self.curr_position[0] - i) == 2 and abs(self.curr_position[1] - j) == 1) or (abs(self.curr_position[0] - i) == 1 and abs(self.curr_position[1] - j) == 2):
                    moveset.append( (i, j) )
        
        return moveset
        
        