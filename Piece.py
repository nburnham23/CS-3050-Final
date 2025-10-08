import arcade


# TODO: Replace scale with constant for all pieces

# TODO: Replace scale with constant for all pieces

class Piece(arcade.Sprite):
    def __init__(self, color, board_position, image_path, scale):
        # Initialize Sprite parent class
        super().__init__(image_path, scale)

        self.color = color
        self.curr_position = board_position
        self.possible_moves = self.calculate_moves()

    def calculate_moves(self):
        # Clear moveset
        self.possible_moves = []

        # Update moveset
        self.possible_moves = self.move(self.curr_position)

    # Move function to be overriden by subclasses
    def move(self):
        pass

    # # Verify and move piece to valid position, recalculate possible moveset from new position
    # def move_to(self, new_position):
    #     if new_position not in self.possible_moves:
    #         return False
        
    #     self.curr_position = new_position
    #     self.calculate_moves()