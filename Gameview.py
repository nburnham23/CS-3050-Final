import arcade
from pieces import Bishop, King, Knight, Pawn, Queen, Rook

ROW_COUNT = 8
COLUMN_COUNT = 8
WIDTH = 80
HEIGHT = 80
MARGIN = 5


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.BLACK
        self.grid = [[None for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]
        self.piece_list = arcade.SpriteList()
        self.setup_board()

    def setup_board(self):
        # Pawns
        for col in range(8):
            self.add_piece(Pawn("white", 1, col))
            self.add_piece(Pawn("black", 6, col))

        # Rooks
        self.add_piece(Rook("white", 0, 0))
        self.add_piece(Rook("white", 0, 7))
        self.add_piece(Rook("black", 7, 0))
        self.add_piece(Rook("black", 7, 7))

        # Knights
        self.add_piece(Knight("white", 0, 1))
        self.add_piece(Knight("white", 0, 6))
        self.add_piece(Knight("black", 7, 1))
        self.add_piece(Knight("black", 7, 6))

        # Bishops
        self.add_piece(Bishop("white", 0, 2))
        self.add_piece(Bishop("white", 0, 5))
        self.add_piece(Bishop("black", 7, 2))
        self.add_piece(Bishop("black", 7, 5))

        # Queens and Kings
        self.add_piece(Queen("white", 0, 3))
        self.add_piece(King("white", 0, 4))
        self.add_piece(Queen("black", 7, 3))
        self.add_piece(King("black", 7, 4))

    def add_piece(self, piece):
        self.grid[piece.row][piece.col] = piece
        self.piece_list.append(piece)

    def on_draw(self):
        self.clear()
        # Draw the checkered board
        for row in range(ROW_COUNT):
            for col in range(COLUMN_COUNT):
                color = arcade.color.BEIGE if (row + col) % 2 == 0 else arcade.color.BISTRE
                x = (MARGIN + WIDTH) * col + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)
        # Draw pieces
        self.piece_list.draw()
