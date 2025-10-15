from pieces.Piece import Piece


class King(Piece):
    def __init__(self, color, row, col):
        img = f"pieceimages/{color}_king.png"
        super().__init__(color, row, col, img)

    def calculate_moves(self, grid):
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1),
                   (1, 1), (1, -1), (-1, 1), (-1, -1)]
        return [(self.row + r, self.col + c) for r, c in offsets]
