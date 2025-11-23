"""
Game class
"""

import Pawn
from Board import Board
import arcade
from MyBot import BotPlayer


class Game:
    """
    Main game logic class for chess
    Class handles turns, moves, check/checkmate, and connects BoardGUI
    """
    def __init__(self, bot=False):
        """
        Initialize a new game
        """
        # Create new chess board
        self.board = Board()
        # Set current turn to white following chess rules
        self.current_turn = "WHITE"
        # Store the winner color
        self.winner = None
        # Track if game is over
        self.is_game_over = False
        # Keeps history of all moves made
        self.move_history = []
        # Optional: bot player
        self.bot_player = BotPlayer("BLACK", self.board) if bot else None
        self.bot_move_pending = False

    # Function to switch the current turn between WHITE and BLACK
    def switch_turn(self):
        if self.current_turn == "WHITE":
            self.current_turn = "BLACK"
        else:
            self.current_turn = "WHITE"

    def trigger_promotion(self, pawn, position):
        from PromotionView import PromotionView

        def receive_promoted_piece(new_piece):
            # replace pawn with new piece in board
            self.board.set_piece(position, new_piece)
            self.switch_turn()

        #TODO: self.gui?
        promotion_view = PromotionView(pawn, receive_promoted_piece, self.gui, position)
        self.gui.window.show_view(promotion_view)

    # Logic for making a move
    def make_move(self, from_position, to_position):
        """
        Check if piece has legal move and if yes moves from_position to to_position on board
        Checks for self check, check/checkmate
        """
        # If game is over no more moves allowed
        if self.is_game_over:
            print("GAME OVER")
            return False

        # Get the piece at the clicked on position
        piece = self.board.get_piece(from_position)
        if piece is None:
            print("NO PIECE SELECTED")
            return False

        # Output piece selected (debug purposes)
        print(f"SELECTED PIECE: {piece.__class__.__name__}")

        # If piece does not belong to current player print error statement
        if piece.piece_color != self.current_turn:
            print("TRIED MOVING PIECE OUT OF TURN")
            return False
            # Validate that to_position in selected pieces moveset
        if to_position not in piece.moveset:
            print("INVALID MOVE FOR PIECE")
            return False

                
        moving_piece = piece
        captured_piece = self.board.get_piece(to_position)
        self.board.set_piece(to_position, moving_piece)
        self.board.set_piece(from_position, None)
        moving_piece.curr_position = to_position
        self.board.calculate_movesets()
        if self.is_in_check(self.current_turn):
            # Undo move
            self.board.set_piece(from_position, moving_piece)
            self.board.set_piece(to_position, captured_piece)
            moving_piece.curr_position = from_position
            self.board.calculate_movesets()
            print("ILLEGAL MOVE: MOVE LEAVES KING IN CHECK")
            return False
        
        self.check_en_passant(from_position, to_position)


        # Make the actual move and append move to move_history
        self.board.move(from_position, to_position)
        self.move_history.append((piece, from_position, to_position))
        # If this pawn moved two squares, mark it
        if isinstance(piece, Pawn.Pawn) and abs(from_position[0] - to_position[0]) == 2:
            piece.just_moved_two = True
        else:
            piece.just_moved_two = False
        # Clear everyone else's just_moved_two
        for r in range(8):
            for c in range(8):
                p = self.board.get_piece((r, c))
                if isinstance(p, Pawn.Pawn) and p != piece:
                    p.just_moved_two = False

        # check for promotion eligibility
        if isinstance(piece, Pawn.Pawn):
            final_row = 0 if piece.piece_color == "BLACK" else 7
            if to_position[0] == final_row:
                self.trigger_promotion(piece, to_position)
                return True
        piece.has_moved = True

        # Determine opponent color
        if self.current_turn == "WHITE":
            enemy_color = "BLACK"
        else:
            enemy_color = "WHITE"

        # Check if the move puts the opponent in check
        if self.is_in_check(enemy_color):
            # If enemy is in checkmate output in terminal
            print(f"{enemy_color} is in CHECK!")
            # Check for checkmate
            if self.is_checkmate(enemy_color):
                self.winner = self.current_turn
                print(f"CHECKMATE! {self.winner} wins!")
                self.is_game_over = True
                return True
            
        # Switch to opponents turn
        self.switch_turn()
        return True

    # Return the position of a piece
    def get_piece(self, position):
        return self.board.get_piece(position)
    
    def find_king(self, color):
        """
        Locates the king of a given color on the board
        Returns the position
        """
        # Loop through each row and column
        for r in range(8):
            for c in range(8):
                piece = self.board.get_piece((r, c))
                # Check if piece is correct color and is the king
                if piece is not None and piece.piece_color == color and piece.__class__.__name__ == "King":
                    return r, c
        return None

    def is_in_check(self, color):
        """
        Returns True if the king of given color is in check
        """
        king_pos = self.find_king(color)
        if not king_pos:
            print("GAME OVER FROM is_in_check")
            return True
        king_piece = self.board.get_piece((king_pos))
        # Determine enemy color
        if color == "WHITE":
            enemy_color = "BLACK"
        else:
            enemy_color = "WHITE"
        # Loop through each row and column
        for r in range(8):
            for c in range(8):
                piece = self.board.get_piece((r, c))
                # Check if piece is in moveset and can attack the king
                if piece and piece.piece_color == enemy_color:
                    if king_pos in piece.moveset:
                        king_piece.in_check = True
                        return True
        king_piece.in_check = False
        return False

    def is_checkmate(self, color):
        """
        Returns True if the given color is in checkmate
        """
        # If not in check can't be checkmate
        if not self.is_in_check(color):
            return False
        # Try every piece belonging to color
        for row in range(8):
            for col in range(8):
                piece = self.board.get_piece((row, col))
                if piece and piece.piece_color == color:
                    # Update moves
                    piece.calculate_moves(self.board)
                    for move in piece.moveset:
                        from_pos = (row, col)
                        to_pos = move
                        # Save the board state before the move
                        moving_piece = self.board.get_piece(from_pos)
                        captured_piece = self.board.get_piece(to_pos)
                        # Perform simulated move
                        self.board.set_piece(to_pos, moving_piece)
                        self.board.set_piece(from_pos, None)
                        moving_piece.curr_position = to_pos
                        # Update all moves after moving
                        self.board.calculate_movesets()
                        # Check wether this simulated move still leaves player in check
                        still_in_check = self.is_in_check(color)
                        # Undo all moves
                        self.board.set_piece(from_pos, moving_piece)
                        self.board.set_piece(to_pos, captured_piece)
                        moving_piece.curr_position = from_pos
                        # Recompoute moves after restoring board state
                        self.board.calculate_movesets()
                        # If move gets out of check, not checkmate
                        if not still_in_check:
                            return False
        return True

    def check_en_passant(self, from_position, to_position):
        # TODO: clean this up, reset all pawns' just_moved_two to False, get possible move to be drawn
        # TODO: alter to return bool repping if en passant is possible that can be called from GameView
        #   and then create another function that actually performs the en passant
        piece = self.board.get_piece(from_position)
        if isinstance(piece, Pawn.Pawn):
            # Pawn moving diagonally to an empty square => possible en passant
            if to_position[1] - from_position[1] in (-1, 1):
                # check to see that to_position is empty
                if self.board.get_piece(to_position) is None:
                    captured_pawn_pos = (from_position[0], to_position[1])
                    captured_piece = self.board.get_piece(captured_pawn_pos)
                    print("move history: ", self.move_history)
                    last_piece, start, end = self.move_history[-1]
                    if last_piece == captured_piece and abs(start[0] - end[0]) == 2:
                        print("last piece moved: ", last_piece)
                        captured_piece.just_moved_two = True
                        piece.calculate_moves(self.board)
                    if captured_piece and isinstance(captured_piece, Pawn.Pawn):
                        self.board.set_piece(captured_pawn_pos, None)
                        if piece.piece_color == "WHITE":
                            self.board.black_taken.append(captured_piece)
                        else:
                            self.board.white_taken.append(captured_piece)

    # Display the board
    def display_board(self):
        self.board.display()

    # Start the game with BoardGUI
    @staticmethod
    def start_game():
        """
        Creat GUI window and show menu
        """
        # Import BoardGUI here to avoid circular import at module import time
        import MenuView

        window = arcade.Window(MenuView.WINDOW_WIDTH, MenuView.WINDOW_HEIGHT, MenuView.WINDOW_TITLE)
        # game = Game()
        menu_view = MenuView.MenuView()
        window.show_view(menu_view)
        arcade.run()

    # Reset game
    def reset_game(self):
        arcade.close_window()
        self.__init__()


def main():
    game = Game()
    game.start_game()


if __name__ == "__main__":
    main()
