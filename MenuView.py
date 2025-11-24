"""
Menu View Module for choosing play mode in a game of chess
"""

import arcade
import arcade.gui
import arcade.gui.widgets.buttons
import arcade.gui.widgets.layout
from MyBot import BotPlayer
from SmartBot import SmartBot
from Game import Game

from constants import (
    BUTTON_WIDTH, COLOR_ALIGN_X, COLOR_ALIGN_Y,
    MENU_TEXT_W, MENU_TEXT_H, MENU_FONT_SIZE)
from GameView import GameView


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
            text="Two-player mode", width=BUTTON_WIDTH
        )
        self.v_box.add(two_player_button)
        two_player_button.on_click = self.on_click_two_player

        ai_easy_button = arcade.gui.widgets.buttons.UIFlatButton(
            text="Player v. Computer: Easy", width=BUTTON_WIDTH
        )
        self.v_box.add(ai_easy_button)
        ai_easy_button.on_click = self.on_click_ai_easy

        ai_hard_button = arcade.gui.widgets.buttons.UIFlatButton(
            text="Player v. Computer: Hard", width=BUTTON_WIDTH
        )
        self.v_box.add(ai_hard_button)
        ai_hard_button.on_click = self.on_click_ai_hard

        quit_button = arcade.gui.widgets.buttons.UIFlatButton(text="Quit", width=300)
        self.v_box.add(quit_button)
        quit_button.on_click = self.on_click_quit

        colors_button = arcade.gui.widgets.buttons.UIFlatButton(
            text="Set Colors", width=BUTTON_WIDTH
        )
        colors_button.on_click = self.on_click_colors_button

        colors_anchor = arcade.gui.widgets.layout.UIAnchorLayout()
        colors_anchor.add(colors_button, anchor_x="left", anchor_y="top",
                          align_x=COLOR_ALIGN_X, align_y=COLOR_ALIGN_Y)

        # Create a widget to hold the v_box widget, that will center the buttons
        ui_anchor_layout = arcade.gui.widgets.layout.UIAnchorLayout()
        ui_anchor_layout.add(child=self.v_box, anchor_x="center_x", anchor_y="center_y")

        self.manager.add(ui_anchor_layout)
        self.manager.add(colors_anchor)

    # Note: event argument must be present for buttons to work
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
        game = Game(bot=True, bot_class=BotPlayer)
        game_view = GameView(game, self.color_one, self.color_two)
        self.window.show_view(game_view)

    def on_click_ai_hard(self, event):
        """ Sets the game mode to Hard AI and creates the Game View """
        print("ai-hard:", event)
        self.manager.disable()
        game = Game(bot=True, bot_class=SmartBot)
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
                         MENU_TEXT_W,
                         MENU_TEXT_H,
                         arcade.color.BLACK,
                         font_size=MENU_FONT_SIZE,
                         anchor_x='center',
                         font_name="Kenney Blocks")
        self.manager.draw()
