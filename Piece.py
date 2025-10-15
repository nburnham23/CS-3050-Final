import arcade

WIDTH = 80
HEIGHT = 80
MARGIN = 5


class Piece(arcade.Sprite):
    def __init__(self, color: str, row: int, col: int, image_path: str):
        super().__init__(image_path, scale=0.4)
        self.color = color  # 'white' or 'black'
        self.row = row
        self.col = col
        self.update_position()

    def update_position(self):
        """Convert row/col to pixel coordinates."""
        x = (MARGIN + WIDTH) * self.col + MARGIN + WIDTH // 2
        y = (MARGIN + HEIGHT) * self.row + MARGIN + HEIGHT // 2
        self.center_x = x
        self.center_y = y

    def calculate_moves(self, grid):
        """Override this in subclasses."""
        return []