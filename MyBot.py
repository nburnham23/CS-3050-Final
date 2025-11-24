"""
Easy Bot class
"""

import random


class BotPlayer:
    def __init__(self, color, board):
        self.color = color
        self.board = board

    def generate_move(self):
        """Make a random valid move (avoiding moves onto own pieces)."""
        # Find all pieces belonging to this bot
        bot_pieces = []
        for row in range(len(self.board.board)):
            for col in range(len(self.board.board[row])):
                piece = self.board.get_piece((row, col))
                if piece is not None and piece.piece_color == self.color:
                    bot_pieces.append((row, col, piece))

        # Make sure movesets are up to date
        self.board.calculate_movesets()

        # Collect all valid moves that don’t capture own pieces
        valid_moves = []
        for row, col, piece in bot_pieces:
            moves = piece.moveset
            for move_row, move_col in moves:
                # Stay within board boundaries
                if 0 <= move_row < 8 and 0 <= move_col < 8:
                    dest_piece = self.board.get_piece((move_row, move_col))
                    # Only allow moving to empty squares or enemy pieces
                    if dest_piece is None or dest_piece.piece_color != self.color:
                        valid_moves.append(((row, col), (move_row, move_col)))

        # If no valid moves, bot skips
        if not valid_moves:
            print(f"{self.color} bot has no valid moves.")
            return None, None, None

        # Choose a random valid move
        start_square, end_square = random.choice(valid_moves)
        print(f"{self.color} bot moving from {start_square} to {end_square}")
        piece = self.board.get_piece(start_square)

        # Execute move on the board
        return piece, start_square, end_square
