"""
testing file to test the board
"""

from Board import Board

def main():
    game = Board()
    # game.display()

    # print(game.get_piece((0, 0)))

    game.move((1, 0), (4, 0))
    game.display()

if __name__ == '__main__':
    main()
