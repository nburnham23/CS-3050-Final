"""
GUI class for when a pawn can be promoted to another piece
"""

import arcade
import arcade.gui
import arcade.gui.widgets.buttons
import arcade.gui.widgets.layout

from Bishop import Bishop
from Board import img_path
from Knight import Knight
from Pawn import Pawn
from Piece import Piece
from Queen import Queen
from Rook import Rook

from constants import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, BUTTON_WIDTH, PROMOTION_FONT_SIZE, PROMOTION_TEXT_W, \
    PROMOTION_TEXT_H
from GameView import GameView
from Game import Game


class PromotionView(arcade.View):
    """
    View to show which pieces can be promoted when a pawn reaches the other side of the board
    """
    def __init__(self, pawn: Pawn, on_promote_callback, game_view: GameView, position):
        super().__init__()
        self.background_color = arcade.color.WHITE
        self.piece_color = pawn.piece_color
        self.position = position
        self.on_promote_callback = on_promote_callback
        self.game_view = game_view
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.widgets.layout.UIBoxLayout(space_between=20)
        # create buttons for each piece that can be promoted
        queen_button = arcade.gui.widgets.buttons.UIFlatButton(
            text="Queen", width=BUTTON_WIDTH
        )
        self.v_box.add(queen_button)
        queen_button.on_click = self.on_click_queen_button

        rook_button = arcade.gui.widgets.buttons.UIFlatButton(
            text="Rook", width=BUTTON_WIDTH
        )
        self.v_box.add(rook_button)
        rook_button.on_click = self.on_click_rook_button

        knight_button = arcade.gui.widgets.buttons.UIFlatButton(
            text="Knight", width=BUTTON_WIDTH
        )
        self.v_box.add(knight_button)
        knight_button.on_click = self.on_click_knight_button

        bishop_button = arcade.gui.widgets.buttons.UIFlatButton(
            text="Bishop", width=BUTTON_WIDTH
        )
        self.v_box.add(bishop_button)
        bishop_button.on_click = self.on_click_bishop_button

        pawn_button = arcade.gui.widgets.buttons.UIFlatButton(
            text="Pawn", width=BUTTON_WIDTH
        )
        self.v_box.add(pawn_button)
        pawn_button.on_click = self.on_click_pawn_button

        # Create a widget to hold the v_box widget, that will center the buttons
        ui_anchor_layout = arcade.gui.widgets.layout.UIAnchorLayout()
        ui_anchor_layout.add(child=self.v_box, anchor_x="center_x", anchor_y="center_y")

        self.manager.add(ui_anchor_layout)

    def on_click_queen_button(self, event):
        print("Queen clicked")
        queen = Queen(self.piece_color, self.position, img_path['queen'][self.piece_color])
        self.on_promote_callback(queen)
        self.manager.disable()
        self.game_view.update_sprites()
        self.window.show_view(self.game_view)

    def on_click_rook_button(self, event):
        print("Rook clicked")
        rook = Rook(self.piece_color, self.position, img_path['rook'][self.piece_color])
        self.on_promote_callback(rook)
        self.manager.disable()
        self.game_view.update_sprites()
        self.window.show_view(self.game_view)

    def on_click_knight_button(self, event):
        # piece_color, start_position, image_path
        print("Knight clicked")
        knight = Knight(self.piece_color, self.position, img_path['knight'][self.piece_color])
        self.on_promote_callback(knight)
        self.manager.disable()
        self.game_view.update_sprites()
        self.window.show_view(self.game_view)

    def on_click_bishop_button(self, event):
        print("Bishop clicked")
        bishop = Bishop(self.piece_color, self.position, img_path['bishop'][self.piece_color])
        self.on_promote_callback(bishop)
        self.manager.disable()
        self.game_view.update_sprites()
        self.window.show_view(self.game_view)

    def on_click_pawn_button(self, event):
        print("Pawn clicked")
        pawn = Pawn(self.piece_color, self.position, img_path['pawn'][self.piece_color])
        self.on_promote_callback(pawn)
        self.manager.disable()
        self.game_view.update_sprites()
        self.window.show_view(self.game_view)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Select a piece to promote",
                         PROMOTION_TEXT_W,
                         PROMOTION_TEXT_H,
                         arcade.color.BLACK,
                         font_size=PROMOTION_FONT_SIZE,
                         anchor_x='center',
                         font_name="Kenney Blocks")
        self.manager.draw()


def main():
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    def test_func(piece: Piece):
        print(f"{type(piece)} selected")

    # Create the MenuView
    promotion_view = PromotionView(Pawn("WHITE", (1,0), img_path['pawn']["WHITE"]),
                                   test_func, GameView(Game()), (0,0))

    # Show GameView on screen
    window.show_view(promotion_view)

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()
