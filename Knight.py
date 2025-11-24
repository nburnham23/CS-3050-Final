"""
Knight class
"""
from Piece import Piece
from constants import BOARD_LENGTH
class Knight(Piece):
    """
    Knight piece class
    """
    def move(self, board):
        """
        Knight move calculation
        """
        moveset = []
        row, col = self.curr_position

        # Vector's of knight's moves
        # Knight can jump over pieces
        directions = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]

        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy

            if 0 <= new_row < BOARD_LENGTH and 0 <= new_col < BOARD_LENGTH:
                target_square = board.get_piece((new_row, new_col))

                if target_square is None or target_square.piece_color != self.piece_color:
                    moveset.append((new_row, new_col))

        return moveset
