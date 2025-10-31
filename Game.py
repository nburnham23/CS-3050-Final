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
        class LinkedBoardGUI(BoardGUI.GameView):
            def __init__(self, game):
                super().__init__()
                self.game = game
                self.chess_board = game.board

            def on_mouse_press(self, x, y, button, modifiers):
                column = int(x // (BoardGUI.WIDTH + BoardGUI.MARGIN))
                row = int(y // (BoardGUI.HEIGHT + BoardGUI.MARGIN))

                if row >= BoardGUI.ROW_COUNT or column >= BoardGUI.COLUMN_COUNT:
                    return

                if self.selected_square:
                    from_pos = self.selected_square
                    to_pos = (row, column)

                    # Attempt the move
                    if self.game.make_move(from_pos, to_pos):
                        # Update piece sprite positions
                        self.update_sprites()

                    # Reset GUI
                    self.reset_color(from_pos[0], from_pos[1])
                    self.reset_color(to_pos[0], to_pos[1])
                    self.selected_square = None
                    self.destination_square = None
                else:
                    piece = self.chess_board.get_piece((row, column))
                    if piece and piece.piece_color == self.game.current_turn:
                        self.selected_square = (row, column)
                        self.grid[row][column] = 2

        window = arcade.Window(BoardGUI.WINDOW_WIDTH, BoardGUI.WINDOW_HEIGHT, BoardGUI.WINDOW_TITLE)
        game = Game()
        game_view = LinkedBoardGUI(game)
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
