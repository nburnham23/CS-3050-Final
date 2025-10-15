import arcade
from Gameview import Gameview

WINDOW_WIDTH = 685
WINDOW_HEIGHT = 685
WINDOW_TITLE = "Chess with Sprites"

def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    view = Gameview()
    window.show_view(view)
    arcade.run()


if __name__ == "__main__":
    main()
