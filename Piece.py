import arcade

# TODO: Replace scale with constant for all pieces

BOARD_LENGTH = 8

class Piece(arcade.Sprite):
    def __init__(self, color, board_position, image_path, scale = 1):
        # Initialize Sprite parent class
        super().__init__(image_path, scale)

        self.color = color
        self.curr_position = board_position
        self.possible_moves = self.calculate_moves()

    def calculate_moves(self):
        # Clear moveset
        self.possible_moves = []

        # Update moveset
        self.possible_moves(self.move(self.curr_position))

    # Move function to be overriden by subclasses
    def move(self):
        pass