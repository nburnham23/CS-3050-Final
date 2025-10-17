"""
Chess Board GUI
CS 3050 Final Project
"""
import arcade
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

# Do the math to figure out our screen dimensions
WINDOW_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
WINDOW_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
WINDOW_TITLE = "Welcome to chess!"


class GameView(arcade.View):
    """
    Main application class.
    """
    def __init__(self):
        """
        Set up the application.
        """

        super().__init__()

        self.chess_board = Board()
        self.sprites = arcade.SpriteList()
        # append each piece sprite to the sprite list
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                piece = self.chess_board.board[row][column]
                if piece is not None:
                    # Set the sprite's position on screen
                    piece.set_sprite_position(MARGIN, WIDTH, HEIGHT)
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
                        self.grid[row].append(0)  # Append a cell
            else:
                for column in range(COLUMN_COUNT):
                    if column % 2 == 1:
                        self.grid[row].append(1)
                    else:
                        self.grid[row].append(0)  # Append a cell

        self.background_color = arcade.color.BLACK
        self.selected_square = None
        self.destination_square = None # the destination for the selected piece

    def reset_color(self, row, column):
        if (row + column) % 2 == 0:
            self.grid[row][column] = 1
        else:
            self.grid[row][column] = 0

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
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                arcade.draw_rect_filled(arcade.rect.XYWH(x, y, WIDTH, HEIGHT), color)
        # draw the pieces
        self.sprites.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        TODO: change to move pieces
        get piece at selected square
        use chess_board move function to move it
        if self.selected piece:
            the mouse press is the destination
            move the piece to the destination
            using the chess_board move function
            then clear the selected piece and the destination
        if not self.selected piece
            select the piece
            color that square green
        """

        # Change the x/y screen coordinates to grid coordinates
        column = int(x // (WIDTH + MARGIN))
        row = int(y // (HEIGHT + MARGIN))

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < ROW_COUNT and column < COLUMN_COUNT:
            """
            if self.selected piece:
                the mouse press is the destination
                move the piece to the destination
                using the chess_board move function
                then clear the selected piece and the destination
                UPDATE POSITION OF SPRITES
            if not self.selected piece
                select the piece
                color that square green
            """
            # there is a piece selected and we can move it
            if self.selected_square:
                prev_row, prev_col = self.selected_square
                # reset the color of the square
                self.reset_color(row, column)
                # reset the color of the previous selected_square if pressing the same square again
                if self.selected_square == (row, column):
                    self.reset_color(row, column)
                    self.selected_square = None
                    return
                self.destination_square = (row, column)
                # change the color of the square
                self.grid[row][column] = 2
                print("destination square: ")
                print(self.destination_square)
                # move the piece to the destination square
                self.chess_board.move(self.selected_square, self.destination_square)
                # reset the color of the selected and destination squares
                self.reset_color(row, column)
                self.reset_color(self.selected_square[0], self.selected_square[1])
                # reset the selected and destination squares to None
                self.selected_square = None
                self.destination_square = None
                # TODO: and update the position of the sprites
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
    game = GameView()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()