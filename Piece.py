import arcade
import os

# TODO: Replace scale with constant for all pieces

BOARD_LENGTH = 8

class Piece(arcade.Sprite):
    def __init__(self, color, board_position, image_path, scale = 1):
        self.piece_color = color
        self.curr_position = board_position
        self.moveset = self.move()

        # Check if file exists
        full_path = os.path.abspath(image_path)
        print(f"Loading: {image_path}")
        print(f"Full path: {full_path}")
        print(f"Exists: {os.path.exists(image_path)}")

        # Initialize Sprite parent class
        super().__init__(image_path, scale)

    def calculate_moves(self):
        # Clear moveset
        self.moveset = []

        # Update moveset
        self.moveset = self.move()

    def set_sprite_position(self, margin, width, height):
        """Set the sprite's screen position based on board position"""
        row, col = self.curr_position
        self.center_x = (margin + width) * col + margin + width // 2
        # Flip the row: arcade's (0,0) is bottom-left, but board array (0,0) is top-left
        self.center_y = (margin + height) * (7 - row) + margin + height // 2

    # Move function to be overriden by subclasses
    def move(self):
        return []