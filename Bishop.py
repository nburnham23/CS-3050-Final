"""
Bishop class
"""
from Piece import Piece, BOARD_LENGTH

class Bishop(Piece):
    def __init__(self, piece_color, start_position, image_path, scale = 1):
        super().__init__(piece_color, start_position, image_path, scale)

    def move(self, board):
        moveset = []
        row, col = self.curr_position

        # Vectors of bishop's move directions
        # in order: southeast, southwest, northwest, northeast
        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

        # get possible square for move
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy

            while 0 <= new_row < BOARD_LENGTH and 0 <= new_col < BOARD_LENGTH:
                target_square = board.get_piece((new_row, new_col))

                if target_square is None:
                    moveset.append((new_row, new_col))
                else:
                    # piece in square
                    if target_square.piece_color != self.piece_color:
                        moveset.append((new_row, new_col))
                    # stop when piece in direction
                    break
                new_row += dx
                new_col += dy

        return moveset