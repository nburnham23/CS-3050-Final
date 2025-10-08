from Pawn import Pawn
from Bishop import Bishop
from Knight import Knight
from Rook import Rook
from Queen import Queen
from King import King


# Board is 8x8 tiles
BOARD_LENGTH, BOARD_WIDTH = 8

# Dictionary for pieces' image paths
img_path = {'pawn': ,
            'knight': ,
            'bishop': ,
            'rook': ,
            'queen': ,
            'king': }

class Board():
    def __init__(self):

        self.board = [ [Rook("BLACK", (0,0), img_path['rook']), Knight("BLACK", (0,1), img_path['knight']), 
                        Bishop("BLACK", (0,2), img_path['bishop']), Queen("BLACK", (0,3), img_path['queen']), 
                        King("BLACK", (0,4), img_path['king']), Bishop("BLACK", (0,5), img_path['bishop']), 
                        Knight("BLACK", (0,6), img_path['knight']), Rook("BLACK", (0,7), img_path['rook'])],
                       [Pawn("BLACK", (1,0), img_path['pawn']), Pawn("BLACK", (1,1), img_path['pawn']), 
                        Pawn("BLACK", (1,2), img_path['pawn']), Pawn("BLACK", (1,3), img_path['pawn']), 
                        Pawn("BLACK", (1,4), img_path['pawn']), Pawn("BLACK", (1,5), img_path['pawn']), 
                        Pawn("BLACK", (1,6), img_path['pawn']), Pawn("BLACK", (1,7), img_path['pawn'])],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [Pawn("WHITE", (6,0), img_path['pawn']), Pawn("WHITE", (6,1), img_path['pawn']), 
                        Pawn("WHITE", (6,2), img_path['pawn']), Pawn("WHITE", (6,3), img_path['pawn']), 
                        Pawn("WHITE", (6,4), img_path['pawn']), Pawn("WHITE", (6,5), img_path['pawn']), 
                        Pawn("WHITE", (6,6), img_path['pawn']), Pawn("WHITE", (6,7), img_path['pawn'])],
                       [Rook("WHITE", (7,0), img_path['rook']), Knight("WHITE", (7,1), img_path['knight']), 
                        Bishop("WHITE", (7,2), img_path['bishop']), Queen("WHITE", (7,3), img_path['queen']), 
                        King("WHITE", (7,4), img_path['king']), Bishop("WHITE", (7,5), img_path['bishop']), 
                        Knight("WHITE", (7,6), img_path['knight']), Rook("WHITE", (7,7), img_path['rook'])] ]
        