"""
King Class
"""
from Piece import Piece
from constants import BOARD_LENGTH, SPRITE_SCALE

class King(Piece):
    def __init__(self, piece_color, start_position, image_path, scale = SPRITE_SCALE):
        super().__init__(piece_color, start_position, image_path, scale)

        # Fields for castling
        self.has_moved = False

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

        # Check for castling moves
        # Castling conditions: king and rook have not moved, squares between are empty
        # TODO: squares between are not under attack, king is not in check
        enemy_color = 'BLACK' if self.piece_color == 'WHITE' else 'WHITE'

        king_in_check = board.square_under_attack(self.curr_position, enemy_color)

        if king_in_check:
            print(f"{self.piece_color} King is in check")
        else:
            print(f"{self.piece_color} King is NOT in check")

        if not self.has_moved and not king_in_check:
            # Kingside castling
            kingside_rook_position = (row, BOARD_LENGTH - 1)
            kingside_rook = board.get_piece(kingside_rook_position)
            # Check if rook is present and hasn't moved
            if kingside_rook.__class__.__name__ == "Rook" and not kingside_rook.has_moved:
                # Check if squares between king and rook are empty
                pathing_squares = [(row, col + 1), (row, col + 2)]
                if all(board.get_piece(s) is None for s in pathing_squares):
                    # Check if squares the king passes through are under attack
                    for square in pathing_squares:
                        if board.square_under_attack(square, enemy_color):
                            break
                    moveset.append((row, col + 2))

            # Queenside castling
            queenside_rook_position = (row, 0)
            queenside_rook = board.get_piece(queenside_rook_position)
            # Check if rook is present and hasn't moved
            if queenside_rook.__class__.__name__ == "Rook" and not queenside_rook.has_moved:
                # Check if squares between king and rook are empty
                pathing_squares = [(row, col - 1), (row, col - 2)]
                if all(board.get_piece(s) is None for s in pathing_squares):
                   # Check if squares the king passes through are under attack
                    for square in pathing_squares:
                        if board.square_under_attack(square, enemy_color):
                            break
                    moveset.append((row, col - 2))

        return moveset
