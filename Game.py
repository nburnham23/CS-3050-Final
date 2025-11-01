from Board import Board
import BoardGUI
import arcade

class Game:
    def __init__(self):
        self.board = Board()
        self.current_turn = "WHITE"
        self.winner = None
        self.is_game_over = False
        self.move_history = []

    # Switch turns
    def switch_turn(self):
        if self.current_turn == "WHITE":
            self.current_turn = "BLACK"
        else:
            self.current_turn = "WHITE"
    
    # Implement logic for making a move
    def make_move(self, from_position, to_position):
        # Game is over no moves to be made
        if self.is_game_over:
            print("GAME OVER")
            return False
        
        # Select piece
        piece = self.board.get_piece(from_position)
        print(f"PIECE SELECTED AT: {from_position}")

        # No piece selected
        if piece is None:
            print("NO PIECE SELECTED")
            return False

        # Debug statement to get what piece
        print(f"SELECTED PIECE: {piece.__class__.__name__}")

        # Turn enforcement
        if piece.piece_color != self.current_turn:
            print("TRIED MOVING PIECE OUT OF TURN")
            return False
        
        if to_position not in piece.moveset:
            print("INVALID MOVE FOR PIECE")
            return False
        
        enemy_piece = self.board.get_piece(to_position)
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

    # Linking BoardGUI with Game logic
    @staticmethod
    def start_game():
        window = arcade.Window(BoardGUI.WINDOW_WIDTH, BoardGUI.WINDOW_HEIGHT, BoardGUI.WINDOW_TITLE)
        game = Game()
        game_view = BoardGUI.MenuView(game.board)
        window.show_view(game_view)
        arcade.run()

    # Reset game
    def reset_game(self):
        self.__init__()

def main():
    game = Game()
    game.start_game()

if __name__ == "__main__":
    main()
