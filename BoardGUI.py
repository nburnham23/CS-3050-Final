"""
Chess Board GUI
CS 3050 Final Project
"""
import arcade
import arcade.gui
import arcade.gui.widgets.buttons
import arcade.gui.widgets.layout
from Board import Board


# Set how many rows and columns we will have
ROW_COUNT = 8
COLUMN_COUNT = 8

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 80
HEIGHT = 80

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5
CAPTURE_MARGIN = 2 # in columns

BOARD_OFFSET_X = (WIDTH + MARGIN) * CAPTURE_MARGIN
BOARD_OFFSET_Y = 0

LEFT_CAPTURE_X = MARGIN + WIDTH // 2
RIGHT_CAPTURE_X = BOARD_OFFSET_X + (WIDTH + MARGIN) * (COLUMN_COUNT + CAPTURE_MARGIN) - WIDTH // 2

BASE_Y = BOARD_OFFSET_Y + MARGIN + HEIGHT // 2

# Do the math to figure out our screen dimensions
WINDOW_WIDTH = (WIDTH + MARGIN) * (COLUMN_COUNT + CAPTURE_MARGIN * 2) + MARGIN
WINDOW_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
WINDOW_TITLE = "Welcome to chess!"

class MenuView(arcade.View):
    """
    Menu class
    Allows the user to select their desired game mode
    TODO: change the on_click_ functions to appropriate functions
    """
    def __init__(self, board: Board):
        super().__init__()
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.background_color = arcade.color.WHITE
        self.board = board

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.widgets.layout.UIBoxLayout(space_between=20)

        # Create the buttons
        two_player_button = arcade.gui.widgets.buttons.UIFlatButton(
            text="Two-player mode", width=300
        )
        self.v_box.add(two_player_button)
        two_player_button.on_click = self.on_click_two_player

        ai_easy_button = arcade.gui.widgets.buttons.UIFlatButton(
            text="Player v. Computer: Easy", width=300
        )
        self.v_box.add(ai_easy_button)
        ai_easy_button.on_click = self.on_click_ai_easy

        ai_hard_button = arcade.gui.widgets.buttons.UIFlatButton(
            text="Player v. Computer: Hard", width=300
        )
        self.v_box.add(ai_hard_button)
        ai_hard_button.on_click = self.on_click_ai_hard

        quit_button = arcade.gui.widgets.buttons.UIFlatButton(text="Quit", width=300)
        self.v_box.add(quit_button)
        quit_button.on_click = self.on_click_quit

        # Create a widget to hold the v_box widget, that will center the buttons
        ui_anchor_layout = arcade.gui.widgets.layout.UIAnchorLayout()
        ui_anchor_layout.add(child=self.v_box, anchor_x="center_x", anchor_y="center_y")

        self.manager.add(ui_anchor_layout)

    def on_click_two_player(self, event):
        """ Sets the game mode to two-player and creates the Game View """
        print("two-player:", event)
        self.manager.disable()
        game_view = GameView(self.board)
        self.window.show_view(game_view)
        # TODO: set mode to two-player
    def on_click_ai_easy(self, event):
        """ Sets the game mode to Easy AI and creates the Game View """
        print("ai-easy:", event)
        self.manager.disable()
        game_view = GameView(self.board)
        self.window.show_view(game_view)
        # TODO: set mode to easy ai
    def on_click_ai_hard(self, event):
        """ Sets the game mode to Hard AI and creates the Game View """
        print("ai-hard:", event)
        self.manager.disable()
        game_view = GameView(self.board)
        self.window.show_view(game_view)
        # TODO: set mode to hard ai
    def on_click_quit(self, event):
        """ Closes the arcade window """
        print('goodbye')
        self.manager.disable()
        arcade.exit()
    def on_draw(self):
        """ draws the menu """
        self.clear()
        self.manager.draw()

class GameView(arcade.View):
    """
    Chess game class.
    """
    def __init__(self, board: Board):
        """
        Set up the application.
        """
        super().__init__()

        self.chess_board = board
        self.sprites = arcade.SpriteList()
        # append each piece sprite to the sprite list
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                piece = self.chess_board.board[row][column]
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
        self.selected_piece = None
        self.possible_moves = None
        self.white_taken_sprites = arcade.SpriteList()
        self.black_taken_sprites = arcade.SpriteList()


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
                piece = self.chess_board.board[row][column]
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
                # TODO: make 12 a constant
                if row_one_index < 12:
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
                # TODO: change 12 to a constant
                if row_one_index < 12:
                    piece.center_x = RIGHT_CAPTURE_X
                    piece.center_y = BASE_Y * row_one_index
                    self.white_taken_sprites.append(piece)
                    row_one_index += 1
                else:
                    piece.center_x = RIGHT_CAPTURE_X - WIDTH
                    piece.center_y = BASE_Y * row_two_index
                    self.white_taken_sprites.append(piece)
                    row_two_index += 1

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
                    color = arcade.color.BEIGE
                elif self.grid[row][column] == 1:
                    color = arcade.color.BISTRE
                else:
                    # cell is Chartreuse if it is selected
                    color = arcade.color.CHARTREUSE

                # Do the math to figure out where the box is
                x = BOARD_OFFSET_X + (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = BOARD_OFFSET_Y + (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                arcade.draw_rect_filled(arcade.rect.XYWH(x, y, WIDTH, HEIGHT), color)
        # draw a circle where the piece can move to
        if self.possible_moves is not None:
            for move in self.possible_moves:
                arcade.draw_circle_filled((MARGIN + WIDTH) * move[1] + MARGIN + WIDTH // 2 + BOARD_OFFSET_X,
                                          (MARGIN + WIDTH) * move[0] + MARGIN + WIDTH // 2,
                                          20, arcade.color.RED)
        # draw the pieces
        self.sprites.draw()
        self.white_taken_sprites.draw()
        self.black_taken_sprites.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        # Change the x/y screen coordinates to grid coordinates
        column = int((x - BOARD_OFFSET_X) // (WIDTH + MARGIN))
        row = int((y - BOARD_OFFSET_Y) // (HEIGHT + MARGIN))

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure that the click is on the board
        if  0 <= row < ROW_COUNT and 0 <= column < COLUMN_COUNT:
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
                moved = self.chess_board.move(self.selected_square, self.destination_square)
                # get the piece at the destination only if the move succeeded
                if moved:
                    self.selected_piece = self.chess_board.get_piece(self.destination_square)
                else:
                    self.selected_piece = None

                # reset the color of the selected and destination squares
                self.reset_color(row, column)
                self.reset_color(self.selected_square[0], self.selected_square[1])
                # reset the selected and destination squares and possible moves to None
                self.selected_square = None
                self.destination_square = None

                # if the move succeeded, update sprite position and sprite list
                if self.selected_piece:
                    self.selected_piece.set_sprite_position()
                    self.update_sprites()
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

def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create the GameView
    menu_view = MenuView(Board())

    # Show GameView on screen
    window.show_view(menu_view)

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()
