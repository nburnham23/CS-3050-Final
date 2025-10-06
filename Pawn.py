import Piece
from Board import BOARD_LENGTH, BOARD_WIDTH

class Pawn(Piece):
    def __init__(self, color, start_position):
        super().__init__(self, color, start_position)
        # Attribute for determining if pawn can move 2 spaces
        self.has_moved = False
    
    def move(self):
        moveset = []
        
        # Moves down rows (positive translation in array) if piece is black, otherwise moves up rows (negative translation)
        moveset.append( (self.curr_position[0] + (1 if self.color == "BLACK" else -1), self.curr_position[1]) )
        if not self.has_moved:
            moveset.append( (self.curr_position[0] + (2 if self.color == "BLACK" else -2), self.curr_position[1]) )
        
        return moveset