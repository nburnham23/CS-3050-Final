import arcade

# TODO: Replace scale with constant for all pieces

BOARD_LENGTH = 8

class Piece(arcade.Sprite):
    def __init__(self, color, board_position, image_path, scale = 1):
        self.piece_color = color
        self.curr_position = board_position
        self.moveset = self.move()

        # Initialize Sprite parent class
        super().__init__(filename = image_path, scale = scale)

    def calculate_moves(self):
        # Clear moveset
        self.moveset = []

        # Update moveset
        self.moveset = self.move()

    # Move function to be overriden by subclasses
    def move(self):
        return []