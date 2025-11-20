"""
Menu View Module for choosing play mode in a game of chess
"""

import arcade
import arcade.gui
import arcade.gui.widgets.buttons
import arcade.gui.widgets.layout

from Game import Game

from GameView import GameView

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
    def __init__(self):
        super().__init__()
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.background_color = arcade.color.WHITE
        self.color_one = arcade.color.BISTRE
        self.color_two = arcade.color.BEIGE


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

        colors_button = arcade.gui.widgets.buttons.UIFlatButton(
            text="Set Colors", width=200
        )
        colors_button.on_click = self.on_click_colors_button

        colors_anchor = arcade.gui.widgets.layout.UIAnchorLayout()
        colors_anchor.add(colors_button, anchor_x="left", anchor_y="top", align_x=20, align_y=-20)

        # Create a widget to hold the v_box widget, that will center the buttons
        ui_anchor_layout = arcade.gui.widgets.layout.UIAnchorLayout()
        ui_anchor_layout.add(child=self.v_box, anchor_x="center_x", anchor_y="center_y")

        self.manager.add(ui_anchor_layout)
        self.manager.add(colors_anchor)

    def on_click_two_player(self, event):
        """ Sets the game mode to two-player and creates the Game View """
        print("two-player:", event)
        self.manager.disable()
        game = Game()
        game_view = GameView(game, self.color_one, self.color_two)
        self.window.show_view(game_view)

    def on_click_ai_easy(self, event):
        """ Sets the game mode to Easy AI and creates the Game View """
        print("ai-easy:", event)
        self.manager.disable()
        game = Game(bot=True)
        game_view = GameView(game, self.color_one, self.color_two)
        self.window.show_view(game_view)

    def on_click_ai_hard(self, event):
        """ Sets the game mode to Hard AI and creates the Game View """
        print("ai-hard:", event)
        self.manager.disable()
        # temporarily using stupid bot
        game = Game(bot=True)
        game_view = GameView(game, self.color_one, self.color_two)
        self.window.show_view(game_view)

    def on_click_colors_button(self, event):
        """shows view to set the colors of the game"""
        from color_view import ColorView
        def set_colors(color_one, color_two):
            self.color_one = color_one
            self.color_two = color_two
        color_view = ColorView(self, set_colors)
        self.window.show_view(color_view)

    def on_click_quit(self, event):
        """ Closes the arcade window """
        print('goodbye')
        self.manager.disable()
        arcade.exit()

    def on_draw(self):
        """ draws the menu """
        self.clear()
        arcade.draw_text("Welcome to chess!",
                         self.window.width / 2,
                         self.window.height / 2 + 200,
                         arcade.color.BLACK,
                         font_size=30,
                         anchor_x='center',
                         font_name="Kenney Blocks")
        self.manager.draw()

def main():
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create the MenuView
    menu_view = MenuView()

    # Show GameView on screen
    window.show_view(menu_view)

    # Start the arcade game loop
    arcade.run()

if __name__ == "__main__":
    main()
