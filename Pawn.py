"""
Pawn class
"""
from Piece import Piece, BOARD_LENGTH

class Pawn(Piece):
    def __init__(self, piece_color, start_position, image_path, scale = 1):
        super().__init__(piece_color, start_position, image_path, scale)
        # Attribute for determining if pawn can move 2 spaces
        self.has_moved = False
        self.promotion_available = False

        super().__init__(piece_color, start_position, image_path, scale)

    def move(self, board):
        moveset = []
        row, col = self.curr_position
        # Black pawns move down (increasing row index), white pawns move up
        direction_forward = 1 if self.piece_color == 'BLACK' else -1

        # one-square move
        new_row = row - direction_forward
        if 0 <= new_row < BOARD_LENGTH and board.get_piece((new_row, col)) is None:
            moveset.append((new_row, col))

        # two-square move if not moved yet
        if not self.has_moved:
            new_row = row - (direction_forward * 2)
            # ensure new_row is within bounds before checking board
            if 0 <= new_row < BOARD_LENGTH and board.get_piece((new_row, col)) is None:
                moveset.append((new_row, col))

        # Captures
        direction_capture = (-1, 1)
        for dx in direction_capture:
            new_row, new_col = row - direction_forward, col + dx
            if 0 <= new_row < BOARD_LENGTH and 0 <= new_col < BOARD_LENGTH:
                target_square = board.get_piece((new_row, new_col))
                if target_square and target_square.piece_color != self.piece_color:
                    moveset.append((new_row, new_col))
        return moveset

    # Checks if pawn has reached end of board and must be promoted
    def check_promotion(self):
        row = self.curr_position[0]
        if row in (0, BOARD_LENGTH - 1):
            self.promotion_available = True
