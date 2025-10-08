import Piece
from Board import BOARD_LENGTH, BOARD_WIDTH

class Queen(Piece):
    def move(self):
        moveset = []
        
        for i in range(BOARD_LENGTH):
            for j in range(BOARD_WIDTH):
                # unlimited diagonal and lateral movements
                if (abs(self.curr_position[0] - i) == abs(self.curr_position[1] - j) and self.curr_position != (i, j)) or (i == self.curr_position[0] or j == self.curr_position[1]):
                    moveset.append( (i, j) )
        
        return moveset