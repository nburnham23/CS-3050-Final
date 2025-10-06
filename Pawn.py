import Piece

class Pawn(Piece):
    def __init__(self, color, start_position):
        super().__init__(self, color, start_position)
        # Attribute for determining if pawn can move 2 spaces
        self.has_moved = False
    
    def move(self):
        moveset = []
        moveset.append((self.curr_position[0] + 1, self.curr_position[1]))
        if not self.has_moved:
            moveset.append((self.curr_position[0] + 2, self.curr_position[1]))
        
        return moveset