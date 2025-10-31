from Piece import Piece, BOARD_LENGTH

class Pawn(Piece):
    def __init__(self, color, start_position, image_path, scale = 1):
        # Attribute for determining if pawn can move 2 spaces
        self.has_moved = False
        promotion_available = False

        super().__init__(color, start_position, image_path, scale)
    
    def move(self, board):
        moveset = []
        row, col = self.curr_position
        direction_forward = 1 if not self.color == 'BLACK' else -1

        # one-square move
        new_row = row + direction_forward
        if 0 <= new_row < BOARD_LENGTH and board.get_piece((new_row, col)) is None:
            moveset.append((new_row, col))

        # two-square move if not moved yet
        if not self.has_moved:
            new_row = row + (direction_forward * 2)
            if board.get_piece((new_row, col)) is None:
                moveset.append((new_row, col))
        
        # Captures
        direction_capture = (-1, 1)
        for dx in direction_capture:
            new_row, new_col = row + direction_forward, col + dx
            if 0 <= new_row < BOARD_LENGTH and 0 <= new_col < BOARD_LENGTH:
                target_square = board.get_piece((new_row, new_col))
                if target_square and target_square.color != self.color:
                    moveset.append((new_row, new_col))
        
        return moveset
    
    # Checks if pawn has reached end of board and must be promoted
    def check_promotion(self):
        row, col = self.curr_position
        if row == 0 or row == BOARD_LENGTH - 1:
            self.promotion_available = True