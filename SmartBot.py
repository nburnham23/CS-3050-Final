"""
SmartBot class
"""
from Piece import Piece
import random
import copy

class SmartBot:
    """
    Smart AI bot for chess using Minimax.
    """
    def __init__(self, color, board, depth=2):
        self.color = color
        self.board = board
        self.depth = depth  # How many moves ahead to evaluate

    def generate_move(self):
        """
        Returns: (piece, from_pos, to_pos)
        """
        best_score = -float('inf')
        best_move = None

        # Loop through all pieces of bot color
        for row in range(8):
            for col in range(8):
                piece = self.board.get_piece((row, col))
                if piece and piece.piece_color == self.color:
                    piece.calculate_moves(self.board)
                    for move in piece.moveset:
                        undo = self.board.simulate_move((row, col), move)
                        score = self.minimax(self.depth - 1, False)
                        undo()
                        if score > best_score:
                            best_score = score
                            best_move = (piece, (row, col), move)

        # If no move found, fallback to random move
        if not best_move:
            all_moves = self.get_all_moves()
            if all_moves:
                return random.choice(all_moves)
            else:
                return None, None, None

        return best_move

    def minimax(self, depth, is_maximizing):
        if depth == 0:
            return self.evaluate_board()

        if is_maximizing:
            best_score = -float('inf')
            for piece, from_pos, to_pos in self.get_all_moves(self.color):
                undo = self.board.simulate_move(from_pos, to_pos)
                score = self.minimax(depth - 1, False)
                undo()
                best_score = max(best_score, score)
            return best_score
        else:
            opponent_color = "WHITE" if self.color == "BLACK" else "BLACK"
            best_score = float('inf')
            for piece, from_pos, to_pos in self.get_all_moves(opponent_color):
                undo = self.board.simulate_move(from_pos, to_pos)
                score = self.minimax(depth - 1, True)
                undo()
                best_score = min(best_score, score)
            return best_score

    def get_all_moves(self, color=None):
        """
        Returns a list of all possible moves for given color.
        Each move is (piece, from_pos, to_pos)
        """
        if color is None:
            color = self.color

        moves = []
        for row in range(8):
            for col in range(8):
                piece = self.board.get_piece((row, col))
                if piece and piece.piece_color == color:
                    piece.calculate_moves(self.board)
                    for move in piece.moveset:
                        moves.append((piece, (row, col), move))
        return moves

    def evaluate_board(self):
        """
        Simple evaluation function: material value only.
        """
        piece_values = {
            "Pawn": 1,
            "Knight": 3,
            "Bishop": 3,
            "Rook": 5,
            "Queen": 9,
            "King": 1000
        }

        score = 0
        for row in range(8):
            for col in range(8):
                piece = self.board.get_piece((row, col))
                if piece:
                    value = piece_values.get(piece.__class__.__name__, 0)
                    if piece.piece_color == self.color:
                        score += value
                    else:
                        score -= value
        return score
