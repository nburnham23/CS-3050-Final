"""
King Class
"""
from Piece import Piece, BOARD_LENGTH

class King(Piece):
    def __init__(self, piece_color, start_position, image_path, scale = 1):
        super().__init__(piece_color, start_position, image_path, scale)

    def move(self, board):
        moveset = []
        row, col = self.curr_position

        # Vectors of queen's move directions
        # in order: southeast, south, southwest, west, northwest, north, northeast, east
        directions = [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]

        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if 0 <= new_row < BOARD_LENGTH and 0 <= new_col < BOARD_LENGTH:
                target_square = board.get_piece((new_row, new_col))
                if target_square is None or target_square.piece_color != self.piece_color:
                    moveset.append((new_row, new_col))
        return moveset
