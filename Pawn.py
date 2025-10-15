from Piece import Piece, BOARD_LENGTH

class Pawn(Piece):
    def __init__(self, color, start_position, image_path, scale):
        super().__init__(self, color, start_position, image_path, scale)
        # Attribute for determining if pawn can move 2 spaces
        self.has_moved = False
        promotion_available = False
    
    def move(self):
        moveset = []
        row, col = self.curr_position
        
        # Moves down rows (positive translation in array) if piece is black, otherwise moves up rows (negative translation)
        moveset.append( (row + (1 if self.color == "BLACK" else -1), col) )
        if not self.has_moved:
            moveset.append( (row + (2 if self.color == "BLACK" else -2), col) )
        
        return moveset
    
    # Checks if pawn has reached end of board and must be promoted
    def check_promotion(self):
        row, col = self.curr_position
        if row == 0 or row == BOARD_LENGTH - 1:
            self.promotion_available = True