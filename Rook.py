from Piece import Piece, BOARD_LENGTH

class Rook(Piece):
    def __init__(self, color, start_position, image_path, scale = .3):
        super().__init__(color, start_position, image_path, scale)

    def move(self):
        moveset = []
        row, col = self.curr_position
        
        for i in range(BOARD_LENGTH):
            for j in range(BOARD_LENGTH):
                # unlimited lateral movement
                if (i == row or j == col) and (i, j) != (row, col):
                    moveset.append( (i, j) )
        
        return moveset