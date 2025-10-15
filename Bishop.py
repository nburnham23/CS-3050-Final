from Piece import Piece, BOARD_LENGTH

class Bishop(Piece):
    def __init__(self, color, start_position, image_path, scale = 1):
        super().__init__(color, start_position, image_path, scale)

    def move(self):
        moveset = []
        row, col = self.curr_position
        
        for i in range(BOARD_LENGTH):
            for j in range(BOARD_LENGTH):
                # unlimited diagonal movement
                if abs(row - i) == abs(col - j) and (row, col) != (i, j):
                    moveset.append( (i, j) )
        
        return moveset