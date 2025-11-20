"""
GUI class for when a pawn can be promoted to another piece
"""

import arcade
import arcade.gui
import arcade.gui.widgets.buttons
import arcade.gui.widgets.layout

from MenuView import MenuView

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
WINDOW_TITLE = "Promotion View Testing"

class ColorView(arcade.View):
    """
    View to show which pieces can be promoted when a pawn reaches the other side of the board
    """
    def __init__(self, menu_view: MenuView, set_colors):
        super().__init__()
        self.background_color = arcade.color.WHITE
        # default colors are beige & bistre
        self.color_one = arcade.color.BEIGE
        self.color_two = arcade.color.BISTRE
        self.menu_view = menu_view
        self.set_colors = set_colors # callback function to set the colors
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.widgets.layout.UIBoxLayout(space_between=20)
        # create buttons for each piece that can be promoted
        brown_beige_button = arcade.gui.widgets.buttons.UIFlatButton(
            text="Brown & Beige", width=300
        )
        self.v_box.add(brown_beige_button)
        brown_beige_button.on_click = self.on_click_brown_beige_button

        white_green_button = arcade.gui.widgets.buttons.UIFlatButton(
            text="White & Green", width=300
        )
        self.v_box.add(white_green_button)
        white_green_button.on_click = self.on_click_white_green_button

        pink_purple_button = arcade.gui.widgets.buttons.UIFlatButton(
            text="Pink & Purple", width=300
        )
        self.v_box.add(pink_purple_button)
        pink_purple_button.on_click = self.on_click_pink_purple_button

        green_gold_button = arcade.gui.widgets.buttons.UIFlatButton(
            text="Green & Gold", width=300
        )
        self.v_box.add(green_gold_button)
        green_gold_button.on_click = self.on_click_green_gold_button

        # Create a widget to hold the v_box widget, that will center the buttons
        ui_anchor_layout = arcade.gui.widgets.layout.UIAnchorLayout()
        ui_anchor_layout.add(child=self.v_box, anchor_x="center_x", anchor_y="center_y")

        self.manager.add(ui_anchor_layout)

    def on_click_brown_beige_button(self, event):
        print("Brown & Beige selected")
        self.color_one = arcade.color.BEIGE
        self.color_two = arcade.color.BISTRE
        self.set_colors(self.color_one, self.color_two)
        self.manager.disable()
        self.window.show_view(self.menu_view)

    def on_click_white_green_button(self, event):
        print("White & Green selected")
        self.color_one = arcade.color.EGGSHELL
        self.color_two = arcade.color.BUD_GREEN
        self.set_colors(self.color_one, self.color_two)
        self.manager.disable()
        self.window.show_view(self.menu_view)

    def on_click_pink_purple_button(self, event):
        print("Pink & Purple selected")
        self.color_one = arcade.color.FLUORESCENT_PINK
        self.color_two = arcade.color.PURPLE
        self.set_colors(self.color_one, self.color_two)
        self.manager.disable()
        self.window.show_view(self.menu_view)

    def on_click_green_gold_button(self, event):
        print("Green & Gold selected")
        self.color_one = arcade.color.BRITISH_RACING_GREEN
        self.color_two = arcade.color.GOLD
        self.set_colors(self.color_one, self.color_two)
        self.manager.disable()
        self.window.show_view(self.menu_view)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Select a color scheme:",
                         self.window.width / 2,
                         self.window.height - 100,
                         arcade.color.BLACK,
                         font_size=30,
                         anchor_x='center',
                         font_name="Kenney Blocks")
        self.manager.draw()


def main():
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create the MenuView
    color_view = ColorView(MenuView())

    # Show GameView on screen
    window.show_view(color_view)

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()
