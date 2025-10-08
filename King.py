import Piece
from Board import BOARD_LENGTH, BOARD_WIDTH

class King(Piece):
    def move(self):
        moveset = []
        
        for i in range(BOARD_LENGTH):
            for j in range(BOARD_WIDTH):
                # 1-space diagonal and lateral movements
                if abs(self.curr_position[0] - i) <= 1 and abs(self.curr_position[1] - j) <= 1 and self.curr_position != (i, j):
                    moveset.append( (i, j) )
        
        return moveset