from Piece import Piece, BOARD_LENGTH

class King(Piece):
    def move(self):
        moveset = []
        row, col = self.curr_position
        
        for i in range(BOARD_LENGTH):
            for j in range(BOARD_LENGTH):
                # 1-space diagonal and lateral movements
                if abs(row - i) <= 1 and abs(col - j) <= 1 and (row, col) != (i, j):
                    moveset.append( (i, j) )
        
        return moveset