import arcade
import arcade.gui
import arcade.gui.widgets.buttons
import arcade.gui.widgets.layout

from MenuView import MenuView

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
WINDOW_TITLE = "Game Over View Testing"

class GameOverView(arcade.View):
    def __init__(self, winner):
        super().__init__()
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.background_color = arcade.color.WHITE
        self.winner = winner

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.widgets.layout.UIBoxLayout(space_between=20)

        # Create the buttons
        play_again_button = arcade.gui.widgets.buttons.UIFlatButton(
            text="Play Again", width=300
        )
        self.v_box.add(play_again_button)
        play_again_button.on_click = self.on_click_play_again

        quit_button = arcade.gui.widgets.buttons.UIFlatButton(
            text="Quit", width=300
        )
        self.v_box.add(quit_button)
        quit_button.on_click = self.on_click_quit

        # Create a widget to hold the v_box widget, that will center the buttons
        ui_anchor_layout = arcade.gui.widgets.layout.UIAnchorLayout()
        ui_anchor_layout.add(child=self.v_box, anchor_x="center_x", anchor_y="center_y")

        self.manager.add(ui_anchor_layout)

    def on_click_play_again(self, event):
        print("play again:", event)
        self.manager.disable()
        self.window.show_view(MenuView())

    def on_click_quit(self, event):
        """ Closes the arcade window """
        print('goodbye')
        self.manager.disable()
        arcade.exit()

    def on_draw(self):
        """ draws the menu """
        self.clear()
        arcade.draw_text(f"{self.winner} WINS!",
                         self.window.width / 2,
                         self.window.height / 2 + 100,
                         arcade.color.BLACK,
                         font_size=30,
                         anchor_x="center",
                         font_name="Kenney Blocks")
        self.manager.draw()

def main():
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create the MenuView
    game_over_view = GameOverView("BLACK")

    # Show GameView on screen
    window.show_view(game_over_view)

    # Start the arcade game loop
    arcade.run()

if __name__ == "__main__":
    main()

