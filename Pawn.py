"""
Pawn class
"""
from Piece import Piece
from constants import BOARD_LENGTH, SPRITE_SCALE

class Pawn(Piece):
    def __init__(self, piece_color, start_position, image_path, scale = SPRITE_SCALE):
        super().__init__(piece_color, start_position, image_path, scale)
        # Attribute for determining if pawn can move 2 spaces
        self.has_moved = False
        self.promotion_available = False
        self.just_moved_two = False

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
                if board.get_piece((row - direction_forward, col)) is None:
                    moveset.append((new_row, col))

        # Regular Captures
        direction_capture = (-1, 1)
        for dx in direction_capture:
            new_row, new_col = row - direction_forward, col + dx
            if 0 <= new_row < BOARD_LENGTH and 0 <= new_col < BOARD_LENGTH:
                target_square = board.get_piece((new_row, new_col))
                if target_square and target_square.piece_color != self.piece_color:
                    moveset.append((new_row, new_col))

        # En passant captures
        for dx in direction_capture:
            adj_col = col + dx
            if 0 <= adj_col <= 7:
                adj_square = (row, adj_col)
                enemy_piece = board.get_piece(adj_square)
                if (enemy_piece and isinstance(enemy_piece, Pawn)
                        and enemy_piece.piece_color != self.piece_color
                        and enemy_piece.just_moved_two):
                    # landing square is diagonally forward into empty space
                    en_passant_row = row - direction_forward
                    en_passant_col = adj_col
                    if board.get_piece((en_passant_row, en_passant_col)) is None:
                        moveset.append((en_passant_row, en_passant_col))
        self.moveset = moveset
        return moveset

    # Checks if pawn has reached end of board and must be promoted
    def check_promotion(self):
        row = self.curr_position[0]
        if row in (0, BOARD_LENGTH - 1):
            self.promotion_available = True
