import arcade
# TODO: Replace scale with constant for all pieces

BOARD_LENGTH = 8
MARGIN = 5
WIDTH = 80
HEIGHT = 80
CAPTURE_MARGIN = 2
BOARD_OFFSET_X = (WIDTH + MARGIN) * CAPTURE_MARGIN
BOARD_OFFSET_Y = 0

class Piece(arcade.Sprite):
    def __init__(self, color, board_position, image_path, scale = 1):
        self.piece_color = color
        self.curr_position = board_position
        self.moveset = self.move()

        # Initialize Sprite parent class
        super().__init__(image_path, scale)

    def calculate_moves(self):
        # Clear moveset
        self.moveset = []

        # Update moveset
        self.moveset = self.move()

    def set_sprite_position(self):
        """Set the sprite's screen position based on board position"""
        row, col = self.curr_position
        self.center_x = BOARD_OFFSET_X + (MARGIN + WIDTH) * col + MARGIN + WIDTH // 2
        self.center_y = BOARD_OFFSET_Y + (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

    # Move function to be overriden by subclasses
    def move(self):
        return []