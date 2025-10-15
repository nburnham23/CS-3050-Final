from Piece import Piece
from Board import BOARD_LENGTH, BOARD_WIDTH

class Queen(Piece):
    def __init__(self, color, start_position, image_path, scale = 1):
        super().__init__(color, start_position, image_path, scale)

    def move(self):
        moveset = []
        row, col = self.curr_position
        
        for i in range(BOARD_LENGTH):
            for j in range(BOARD_WIDTH):
                # unlimited diagonal and lateral movements
                if (abs(row - i) == abs(col - j) and (row, col) != (i, j)) or (i == row or j == col):
                    moveset.append( (i, j) )
        
        return moveset