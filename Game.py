from Board import Board
from BoardGUI import ChessWindow

class Game:
    def __init__(self):
        self.board = Board()
        self.current_turn = "WHITE"
        self.winner = None
        self.is_game_over = False
        self.move_history = []

    def switch_turn(self):
        if self.current_turn == "WHITE":
            self.current_turn == "BLACK"
        else:
            self.current_turn == "WHITE"
    
    def make_move(self, from_position, to_position):
        # If the game is over no pieces can be moved
        if self.is_game_over:
            print("Game is over.")
            return False
        
        # No piece at selected index
        piece = self.board.get_piece(from_position)
        if piece is None:
            print("No piece at the starting position")
            return False
        
        # Player choses the wrong color piece
        if piece.piece_color != self.current_turn:
            print("Wrong piece")
            return False
        
        # Player tries moving a piece to a position not in moveset for the piece
        if to_position not in piece.moveset:
            print("Invalid move for this piece")
            return False
        
        # Perform the move on the piece
        enemy_piece = self.board.get_piece(to_position)
        if enemy_piece and enemy_piece.__class__.__name__ == "King":
            self.winner = self.current_turn
            self.is_game_over = True
        
        self.board.move(from_position, to_position)
        self.move_history.append((piece, from_position, to_position))
        self.switch_turn()
        return True
    
    # Return the position of a piece
    def get_piece(self, position):
        return self.board.get_piece(position)

    # Display the board
    def display_board(self):
        self.board.display()

    def reset_game(self):
        self.__init__()

        


