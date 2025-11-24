"""
SmartBot class
"""
import random

class SmartBot:
    """
    Smart AI bot for chess using Minimax.
    Smarter evaluation with positional bonuses and randomized tie-breaking.
    """
    def __init__(self, color, board, depth=2):
        self.color = color
        self.board = board
        self.depth = depth  # how many moves ahead to evaluate

    def generate_move(self):
        """
        Returns (piece, from_pos, to_pos)
        Chooses randomly among equally good moves to avoid repetition.
        """
        best_score = -float('inf')
        best_moves = []

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
                            best_moves = [(piece, (row, col), move)]
                        elif score == best_score:
                            best_moves.append((piece, (row, col), move))

        if best_moves:
            return random.choice(best_moves)
        else:
            # fallback to any move if no "best" found
            all_moves = self.get_all_moves()
            return random.choice(all_moves) if all_moves else (None, None, None)

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
            opponent = "WHITE" if self.color == "BLACK" else "BLACK"
            best_score = float('inf')
            for piece, from_pos, to_pos in self.get_all_moves(opponent):
                undo = self.board.simulate_move(from_pos, to_pos)
                score = self.minimax(depth - 1, True)
                undo()
                best_score = min(best_score, score)
            return best_score

    def get_all_moves(self, color=None):
        if color is None:
            color = self.color
        moves = []
        for r in range(8):
            for c in range(8):
                piece = self.board.get_piece((r, c))
                if piece and piece.piece_color == color:
                    piece.calculate_moves(self.board)
                    for move in piece.moveset:
                        moves.append((piece, (r, c), move))
        return moves

    def evaluate_board(self):
        """
        Enhanced evaluation: material + positional bonuses.
        """
        piece_values = {"Pawn": 1, "Knight": 3, "Bishop": 3, "Rook": 5, "Queen": 9, "King": 1000}

        # Positional bonuses encourage center control and development
        positional_bonus = {
            "Pawn": lambda r, c: 0.3 * (3.5 - abs(3.5 - c)),  # central pawns better
            "Knight": lambda r, c: 0.3 if 2 <= r <= 5 and 2 <= c <= 5 else 0,
            "Bishop": lambda r, c: 0.2,
            "Rook": lambda r, c: 0.1 if r in [0,7] or c in [0,7] else 0,
            "Queen": lambda r, c: 0.1,
            "King": lambda r, c: -0.5 if r < 3 or r > 4 else 0  # prefer safer ranks
        }

        score = 0
        for r in range(8):
            for c in range(8):
                piece = self.board.get_piece((r, c))
                if piece:
                    val = piece_values.get(piece.__class__.__name__, 0)
                    bonus = positional_bonus.get(piece.__class__.__name__, lambda r,c: 0)(r, c)
                    if piece.piece_color == self.color:
                        score += val + bonus
                    else:
                        score -= val + bonus
        return score
