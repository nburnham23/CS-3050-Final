from pieces.Piece import Piece

class Pawn(Piece):
    def __init__(self, color, row, col):
        img = f"pieceimages/{color}_pawn.png"
        super().__init__(color, row, col, img)
        self.has_moved = False

    def calculate_moves(self, grid):
        moves = []
        direction = 1 if self.color == "white" else -1
        moves.append((self.row + direction, self.col))
        if not self.has_moved:
            moves.append((self.row + 2 * direction, self.col))
        return moves