import Piece

class Pawn(Piece):
    def move(self):
        moveset = []
        
        for i in range(BOARD_LENGTH):
            for j in range(BOARD_WIDTH):
                if abs(self.curr_position[0] + i) == abs(self.curr_position[1] + j) and self.curr_position != (i, j):
                    moveset.append( (i, j) )
        
        return moveset