import arcade

class Piece(arcade.Sprite):
    def __init__(self, color, start_position):
        self.color = color
        self.start_position, self.curr_position = start_position
        self.possible_moves = []

    def calculate_moves(self):
        # Clear moveset
        self.possible_moves = []

        # Update moveset
        self.possible_moves(self.move(self.curr_position))

    # Move function to be overriden by subclasses
    def move(self):
        pass