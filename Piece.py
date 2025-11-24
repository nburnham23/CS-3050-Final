"""
Piece class
"""
import arcade
from constants import SPRITE_SCALE, BOARD_OFFSET_X, MARGIN, WIDTH, BOARD_OFFSET_Y, HEIGHT

class Piece(arcade.Sprite):
    """
    Parent class for all chess pieces
    """
    def __init__(self, piece_color, board_position, image_path, scale = SPRITE_SCALE):
        self.piece_color = piece_color
        self.curr_position = board_position
        self.moveset = []

        # Initialize Sprite parent class
        super().__init__(image_path, scale)

    def calculate_moves(self, board):
        """
        Calculate the moveset for this piece based on its type and current board state"""
        # Clear moveset
        self.moveset = []

        # Update moveset
        # Pass the Board object to the subclass move() implementation
        self.moveset = self.move(board)

    def set_sprite_position(self):
        """Set the sprite's screen position based on board position"""
        row, col = self.curr_position
        self.center_x = BOARD_OFFSET_X + (MARGIN + WIDTH) * col + MARGIN + WIDTH // 2
        self.center_y = BOARD_OFFSET_Y + (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

    # Move function to be overriden by subclasses
    def move(self, board):
        """
        Placeholder move function to be overridden by subclasses
        """
        return []
