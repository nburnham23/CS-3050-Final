"""
GUI class for the game of chess
"""
import arcade
import arcade.gui
import arcade.gui.widgets.buttons
import arcade.gui.widgets.layout

import random

from Piece import Piece
from constants import ROW_COUNT, COLUMN_COUNT, LEFT_CAPTURE_X, BASE_Y, RIGHT_CAPTURE_X, WIDTH, BOARD_OFFSET_X, MARGIN, \
    BOARD_OFFSET_Y, HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, CAPTURED_PIECE_LIMIT, PLAYER_TURN_BOX_W, \
    PLAYER_TURN_BOX_H, PLAYER_TURN_TEXT_H, PLAYER_TURN_TEXT_W
from Game import Game


class GameView(arcade.View):
    """
    Chess game class.
    """
    def __init__(self, game: Game, color_one, color_two):
        """
        Set up the application.
        """
        super().__init__()
        self.game = game
        self.chess_board = game.board
        self.game = game
        self.chess_board = game.board
        self.sprites = arcade.SpriteList()
        self.color_one = color_one
        self.color_two = color_two
        self.last_move_start = None
        self.last_move_end = None

        # append each piece sprite to the sprite list
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                piece = self.chess_board.get_piece((row, column))
                if piece is not None:
                    # Set the sprite's position on screen
                    piece.set_sprite_position()
                    self.sprites.append(piece)

        # Create a 2 dimensional array.
        self.grid = []
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell in this row
            self.grid.append([])
            # Mark the which color to make each cell
            if row % 2 == 0:
                for column in range(COLUMN_COUNT):
                    if column % 2 == 0:
                        self.grid[row].append(1)
                    else:
                        self.grid[row].append(0)
            else:
                for column in range(COLUMN_COUNT):
                    if column % 2 == 1:
                        self.grid[row].append(1)
                    else:
                        self.grid[row].append(0)

        self.background_color = arcade.color.CHARCOAL

        self.selected_square = None
        self.destination_square = None # the destination for the selected piece
        self.bot_selected_square = None
        self.bot_destination_square = None # the destination for the bot's selected piece

        self.selected_piece = None
        self.bot_selected_piece = None # the bot's selected piece

        self.possible_moves = None

        self.castled_rook = None # the rook that moved during castling, if any

        self.white_taken_sprites = arcade.SpriteList()
        self.black_taken_sprites = arcade.SpriteList()
        self.game.gui = self


    def reset_color(self, row, column):
        """
        resets the color of a square on the grid depending on its position
        """
        if (row + column) % 2 == 0:
            self.grid[row][column] = 1
        else:
            self.grid[row][column] = 0

    def update_sprites(self):
        """
        resets the sprites to the pieces that are still in the game (not taken)
        """
        self.sprites = arcade.SpriteList()
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                piece = self.chess_board.get_piece((row, column))
                if piece is not None:
                    # Set the sprite's position on screen
                    piece.set_sprite_position()
                    self.sprites.append(piece)
        self.white_taken_sprites = arcade.SpriteList()
        row_one_index = 1
        row_two_index = 1
        for piece in self.chess_board.white_taken:
            if piece is not None:
                # create two columns of captured pieces
                if row_one_index < CAPTURED_PIECE_LIMIT:
                    piece.center_x = LEFT_CAPTURE_X
                    piece.center_y = BASE_Y * row_one_index
                    self.white_taken_sprites.append(piece)
                    row_one_index += 1
                else:
                    piece.center_x = LEFT_CAPTURE_X * 3
                    piece.center_y = BASE_Y * row_two_index
                    self.white_taken_sprites.append(piece)
                    row_two_index += 1
        self.black_taken_sprites = arcade.SpriteList()
        row_one_index = 1
        row_two_index = 1
        for piece in self.chess_board.black_taken:
            if piece is not None:
                # create two columns of captured pieces
                if row_one_index < CAPTURED_PIECE_LIMIT:
                    piece.center_x = RIGHT_CAPTURE_X
                    piece.center_y = BASE_Y * row_one_index
                    self.white_taken_sprites.append(piece)
                    row_one_index += 1
                else:
                    piece.center_x = RIGHT_CAPTURE_X - WIDTH
                    piece.center_y = BASE_Y * row_two_index
                    self.white_taken_sprites.append(piece)
                    row_two_index += 1

    def filter_moveset(self, piece: Piece):
        filtered_moveset = []
        moving_piece = piece
        from_position = moving_piece.curr_position
        for move in piece.moveset:
            potential_check = False
            captured_piece = self.chess_board.get_piece(move)
            self.chess_board.set_piece(move, moving_piece)
            self.chess_board.set_piece(from_position, None)
            moving_piece.curr_position = move
            self.chess_board.calculate_movesets()
            if self.game.is_in_check(self.game.current_turn):
                potential_check = True
            # Undo move
            self.chess_board.set_piece(from_position, moving_piece)
            self.chess_board.set_piece(move, captured_piece)
            moving_piece.curr_position = from_position
            self.chess_board.calculate_movesets()
            if not potential_check:
                filtered_moveset.append(move)
        return filtered_moveset

    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        self.clear()

        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # Color the cells in Beige, Bistre, or Chartreuse according to position / state
                if self.grid[row][column] == 0:
                    color = self.color_one
                elif self.grid[row][column] == 1:
                    color = self.color_two
                else:
                    # cell is Chartreuse if it is selected
                    color = arcade.color.CHARTREUSE
                
                # Highlight last move squares
                if (row, column) == self.last_move_start or (row, column) == self.last_move_end:
                    color = arcade.color.BITTER_LEMON

                # Do the math to figure out where the box is
                x = BOARD_OFFSET_X + (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = BOARD_OFFSET_Y + (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                arcade.draw_rect_filled(arcade.rect.XYWH(x, y, WIDTH, HEIGHT), color)
        # draw a circle where the piece can move to
        curr_turn = self.game.current_turn
        if (self.possible_moves is not None and self.selected_piece is not None and
                self.selected_piece.piece_color == curr_turn):
            for move in self.possible_moves:
                arcade.draw_circle_filled((MARGIN + WIDTH) * move[1] + MARGIN + WIDTH // 2 +
                                          BOARD_OFFSET_X,
                                          (MARGIN + WIDTH) * move[0] + MARGIN + WIDTH // 2,
                                          20, arcade.color.RED)
        # draw the pieces
        self.sprites.draw()
        self.white_taken_sprites.draw()
        self.black_taken_sprites.draw()
        # draw a box with whose turn it is
        arcade.draw_rect_filled(arcade.rect.XYWH(
            PLAYER_TURN_BOX_W,
            PLAYER_TURN_BOX_H,
            250,
            100),
            arcade.color.WHITE)
        arcade.draw_text(
        f"{curr_turn}'s turn",
             PLAYER_TURN_TEXT_W,
             PLAYER_TURN_TEXT_H,
             arcade.color.BLACK,
             font_size=15,
             anchor_x='center',
             font_name="Kenney Blocks"
        )

    def on_mouse_press(self, x, y, button, modifiers):
        # if bot is making a move, ignore player input
        if self.game.bot_move_pending:
            return

        # Change the x/y screen coordinates to grid coordinates
        column = int((x - BOARD_OFFSET_X) // (WIDTH + MARGIN))
        row = int((y - BOARD_OFFSET_Y) // (HEIGHT + MARGIN))

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure that the click is on the board
        if 0 <= row < ROW_COUNT and 0 <= column < COLUMN_COUNT:
            # there is a piece selected and we can move it
            if self.selected_square:
                # reset the color of the square
                self.reset_color(row, column)
                # reset the color of the previous selected_square if pressing the same square again
                if self.selected_square == (row, column):
                    self.reset_color(row, column)
                    self.selected_square = None
                    self.possible_moves = None
                    return
                self.destination_square = (row, column)
                print("destination square: ")
                print(self.destination_square)
                # attempt to move the piece to the destination square
                moved = self.game.make_move(self.selected_square, self.destination_square)
                # get the piece at the destination only if the move succeeded
                if moved:
                    self.last_move_start = self.selected_square
                    self.last_move_end = self.destination_square
                    self.update_sprites()
                    self.selected_piece = self.chess_board.get_piece(self.destination_square)
                    if self.game.is_game_over:
                        from GameOverView import GameOverView
                        game_over_view = GameOverView(self.game.winner)
                        self.window.show_view(game_over_view)
                        return
                    # Check if castling was performed, and update rook sprite position if so
                    if self.selected_piece.__class__.__name__ == 'King' and self.destination_square[1] - self.selected_square[1] == 2:
                        # Kingside castling
                        self.castled_rook = self.chess_board.get_piece((self.destination_square[0], self.destination_square[1] - 1))
                        self.castled_rook.set_sprite_position()
                    if self.selected_piece.__class__.__name__ == 'King' and self.destination_square[1] - self.selected_square[1] == -2:
                        # Queenside castling
                        self.castled_rook = self.chess_board.get_piece((self.destination_square[0], self.destination_square[1] + 1))
                        self.castled_rook.set_sprite_position()
                else:
                    self.selected_piece = None

                # reset the color of the selected and destination squares
                self.reset_color(row, column)
                self.reset_color(self.selected_square[0], self.selected_square[1])
                # reset the selected and destination squares and possible moves to None
                self.selected_square = None
                self.destination_square = None
                self.possible_moves = None

                self.game.display_board()

                # if the move succeeded, update sprite position and sprite list
                if self.selected_piece:
                    self.selected_piece.set_sprite_position()
                    self.update_sprites()

                    if self.castled_rook:
                        self.castled_rook = None

                    # if bot is playing, make bot move
                    if self.game.bot_player and moved:
                        # lock player input until bot move is complete
                        self.game.bot_move_pending = True
                        # make random time delay between 1-2 seconds to pretend bot is thinking
                        delay_time = random.uniform(1, 2)

                        # create bot move function to be scheduled after delay
                        def bot_move_func(dt):
                            try:
                                moved = False
                                while not moved:
                                    self.bot_selected_piece, self.bot_selected_square, self.bot_destination_square = self.game.bot_player.generate_move()
                                    print(f"Bot selected square: {self.bot_selected_square} containing {self.bot_selected_piece}, destination square: {self.bot_destination_square}")
                                    if self.bot_selected_piece:
                                        # bot moved, update its board state again and sprites
                                        moved = self.game.make_move(self.bot_selected_square, self.bot_destination_square)

                                self.last_move_start = self.bot_selected_square
                                self.last_move_end = self.bot_destination_square

                                self.bot_selected_piece.set_sprite_position()
                                self.update_sprites()
                            except Exception as e:
                                print(f"Error during bot move: {e}")
                            self.game.bot_move_pending = False
                            # ensures bot_move_func only runs once
                            arcade.unschedule(bot_move_func)
                        arcade.schedule(bot_move_func, delay_time)

                else:
                    print("Move failed; no piece at destination or invalid move")

            # the user has not selected a piece, so the user will select one
            else:
                # select the piece
                # and color that square green
                self.selected_square = (row, column)
                print(self.selected_square)
                self.grid[row][column] = 2
                print("selected square: " )
                print(self.selected_square)
                piece = self.chess_board.get_piece((row, column))
                piece.move(self.chess_board)
                self.possible_moves = self.filter_moveset(piece)
                self.selected_piece = piece

def main():
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create the MenuView
    game_view = GameView(Game())

    # Show GameView on screen
    window.show_view(game_view)

    # Start the arcade game loop
    arcade.run()

if __name__ == "__main__":
    main()