from pieces.Piece import Piece

class Bishop(Piece):
    def __init__(self, color, row, col):
        img = f"pieceimages/{color}_bishop.png"
        super().__init__(color, row, col, img)

    def calculate_moves(self, grid):
        moves = []
        for i in range(1, 8):
            moves += [
                (self.row + i, self.col + i),
                (self.row - i, self.col + i),
                (self.row + i, self.col - i),
                (self.row - i, self.col - i)
            ]
        return moves
