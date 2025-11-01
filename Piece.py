import arcade
# TODO: Replace scale with constant for all pieces

BOARD_LENGTH = 8
MARGIN = 5
WIDTH = 80
HEIGHT = 80

class Piece(arcade.Sprite):
    def __init__(self, piece_color, board_position, image_path, scale = 1):
        self.piece_color = piece_color
        self.curr_position = board_position
        self.moveset = []

        # Initialize Sprite parent class
        super().__init__(image_path, scale)

    def calculate_moves(self, board):
        # Clear moveset
        self.moveset = []

        # Update moveset
        # Pass the Board object to the subclass move() implementation
        self.moveset = self.move(board)

    def set_sprite_position(self):
        """Set the sprite's screen position based on board position"""
        row, col = self.curr_position
        self.center_x = (MARGIN + WIDTH) * col + MARGIN + WIDTH // 2
        self.center_y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

    # Move function to be overriden by subclasses
    def move(self, board):
        return []