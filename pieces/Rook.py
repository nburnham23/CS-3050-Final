from pieces.Piece import Piece

class Rook(Piece):
    def __init__(self, color, row, col):
        img = f"pieceimages/{color}_rook.png"
        super().__init__(color, row, col, img)

    def calculate_moves(self, grid):
        moves = []
        for i in range(8):
            if i != self.row:
                moves.append((i, self.col))
            if i != self.col:
                moves.append((self.row, i))
        return moves