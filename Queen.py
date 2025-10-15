from Piece import Piece, BOARD_LENGTH

class Queen(Piece):
    def move(self):
        moveset = []
        row, col = self.curr_position
        
        for i in range(BOARD_LENGTH):
            for j in range(BOARD_LENGTH):
                # unlimited diagonal and lateral movements
                if (abs(row - i) == abs(col - j) and (row, col) != (i, j)) or (i == row or j == col):
                    moveset.append( (i, j) )
        
        return moveset