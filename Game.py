from Board import Board
import BoardGUI
import arcade
import copy

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
        if self.is_game_over:
            print("GAME OVER")
            return False

        piece = self.board.get_piece(from_position)
        if piece is None:
            print("NO PIECE SELECTED")
            return False

        print(f"SELECTED PIECE: {piece.__class__.__name__}")

        if piece.piece_color != self.current_turn:
            print("TRIED MOVING PIECE OUT OF TURN")
            return False

        if to_position not in piece.moveset:
            print("INVALID MOVE FOR PIECE")
            return False

        # simulate move to check for self-check
        # TODO: FIND SOLUTION THAT DOESN'T INCLUDE COPIES
        """ test_board = copy.deepcopy(self.board)
        test_board.move(from_position, to_position)
        temp_game = Game()
        temp_game.board = test_board
        if temp_game.is_in_check(self.current_turn):
            print("ILLEGAL MOVE — KING WOULD BE IN CHECK")
            return False """

        # make the actual move
        self.board.move(from_position, to_position)
        self.move_history.append((piece, from_position, to_position))

        # check opponent status
        if self.current_turn == "WHITE":
            enemy_color = "BLACK"
        else:
            enemy_color = "WHITE"

        if self.is_in_check(enemy_color):
            print(f"{enemy_color} is in CHECK!")

            if self.is_checkmate(enemy_color):
                print(f"CHECKMATE! {self.current_turn} wins!")
                self.winner = self.current_turn
                self.is_game_over = True
                return True

        self.switch_turn()
        return True
    
    # Return the position of a piece
    def get_piece(self, position):
        return self.board.get_piece(position)
    
    def find_king(self, color):
        for r in range(8):
            for c in range(8):
                piece = self.board.get_piece((r, c))
                if piece is not None and piece.piece_color == color and piece.__class__.__name__ == "King":
                    return (r, c)
        return None
    
    # Return true if king is in check
    def is_in_check(self, color):
        king_pos = self.find_king(color)
        if not king_pos:
            return False
        
        enemy_color = "BLACK" if color == "WHITE" else "WHITE"

        for r in range(8):
            for c in range(8):
                piece = self.board.get_piece((r, c))
                if piece and piece.piece_color == enemy_color:
                    piece.calculate_moves(self.board)
                    if king_pos in piece.moveset:
                        return True
        return False
    
    def is_checkmate(self, color):
        if not self.is_in_check(color):
            return False
        
        # test every possible move for all pieces of that color
        for r in range(8):
            for c in range(8):
                piece = self.board.get_piece((r, c))
                if piece and piece.piece_color == color:
                    for move in piece.moveset:
                        test_board = copy.deepcopy(self.board)
                        test_board.move((r, c), move)
                        # temp wrap board in dummy game
                        temp_game = Game()
                        temp_game.board = test_board
                        if not temp_game.is_in_check(color):
                            return False
        return True

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
