from Board import Board
from BoardGUI import GameView

class Game:
    def __init__(self):
        board = Board()

        self.white_taken = []
        self.black_taken = []

        self.white_in_check = False
        self.black_in_check = False

    def make_move(self, start_pos, end_pos):
        pass

    def is_valid_move(self, start_pos, end_pos):
        pass

    def check_for_check(self, player):
        pass

    def check_for_checkmate(self, player):
        pass

    def check_for_stalemate(self, player):
        pass

    def switch_player(self):
        pass

    def display_board(self):
        pass

# TODO: Castling, En passant, pawn promotion
