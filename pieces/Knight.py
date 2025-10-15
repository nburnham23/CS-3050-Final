from pieces.Piece import Piece

class Knight(Piece):
    def __init__(self, color, row, col):
        img = f"pieceimages/{color}_knight.png"
        super().__init__(color, row, col, img)

    def calculate_moves(self, grid):
        offsets = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                   (-2, -1), (-1, -2), (1, -2), (2, -1)]
        return [(self.row + r, self.col + c) for r, c in offsets]