from Piece import Piece, BOARD_LENGTH

class Rook(Piece):
    def move(self):
        moveset = []
        row, col = self.curr_position
        
        for i in range(BOARD_LENGTH):
            for j in range(BOARD_LENGTH):
                # unlimited lateral movement
                if i == row or j == col:
                    moveset.append( (i, j) )
        
        return moveset