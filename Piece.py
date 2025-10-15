import arcade

class Piece(arcade.Sprite):
    def __init__(self, image_file, center_x, center_y, color, start_position, piece_type):
        super().__init__(image_file, center_x=center_x, center_y=center_y)
        self.color = color
        self.piece_type = piece_type
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

white_pawn = Piece('white_pawn.png', 0, 0)