"""
Bishop class
"""
from Piece import Piece
from constants import BOARD_LENGTH

class Bishop(Piece):
    """
    Bishop piece class
    """

    def move(self, board):
        """
        Bishop move calculation
        """
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
