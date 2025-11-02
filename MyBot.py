import random
import time

class BotPlayer:
    def __init__(self, color, board):
        self.color = color
        self.board = board

    def make_move(self):
        """Make a random valid move (avoiding moves onto own pieces)."""
        # Find all pieces belonging to this bot
        bot_pieces = []
        for row in range(len(self.board.board)):
            for col in range(len(self.board.board[row])):
                piece = self.board.board[row][col]
                if piece is not None and piece.piece_color == self.color:
                    bot_pieces.append((row, col, piece))

        # Collect all valid moves that don’t capture own pieces
        valid_moves = []
        for row, col, piece in bot_pieces:
            moves = piece.move()
            for move_row, move_col in moves:
                # Stay within board boundaries
                if 0 <= move_row < len(self.board.board) and 0 <= move_col < len(self.board.board):
                    dest_piece = self.board.board[move_row][move_col]
                    # Only allow moving to empty squares or enemy pieces
                    if dest_piece is None or dest_piece.piece_color != self.color:
                        valid_moves.append(((row, col), (move_row, move_col)))

        # If no valid moves, bot skips
        if not valid_moves:
            print(f"{self.color} bot has no valid moves.")
            return

        # Choose a random valid move
        start_square, end_square = random.choice(valid_moves)
        print(f"{self.color} bot moving from {start_square} to {end_square}")

        # Execute move on the board
        self.board.move(start_square, end_square)
