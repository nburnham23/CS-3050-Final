from Pawn import Pawn
from Bishop import Bishop
from Knight import Knight
from Rook import Rook
from Queen import Queen
from King import King


# Board is 8x8 tiles
BOARD_LENGTH, BOARD_WIDTH = 8

# Dictionary for pieces' image paths
img_path = {'pawn': {'BLACK': 'pieceimages/black_pawn.png',
                     'WHITE': 'pieceimages/white_pawn.png'},
            'knight': {'BLACK': 'pieceimages/black_knight.png',
                     'WHITE': 'pieceimages/white_knight.png'},
            'bishop': {'BLACK': 'pieceimages/black_bishop.png',
                     'WHITE': 'pieceimages/white_bishop.png'},
            'rook': {'BLACK': 'pieceimages/black_rook.png',
                     'WHITE': 'pieceimages/white_rook.png'},
            'queen': {'BLACK': 'pieceimages/black_queen.png',
                     'WHITE': 'pieceimages/white_queen.png'},
            'king': {'BLACK': 'pieceimages/black_king.png',
                     'WHITE': 'pieceimages/white_king.png'}}

class Board():
    def __init__(self):

        self.board = [ [Rook("BLACK", (0,0), img_path['rook']["BLACK"]), Knight("BLACK", (0,1), img_path['knight']["BLACK"]), 
                        Bishop("BLACK", (0,2), img_path['bishop']["BLACK"]), Queen("BLACK", (0,3), img_path['queen']["BLACK"]), 
                        King("BLACK", (0,4), img_path['king']["BLACK"]), Bishop("BLACK", (0,5), img_path['bishop']["BLACK"]), 
                        Knight("BLACK", (0,6), img_path['knight']["BLACK"]), Rook("BLACK", (0,7), img_path['rook']["BLACK"])],
                       [Pawn("BLACK", (1,0), img_path['pawn']["BLACK"]), Pawn("BLACK", (1,1), img_path['pawn']["BLACK"]), 
                        Pawn("BLACK", (1,2), img_path['pawn']["BLACK"]), Pawn("BLACK", (1,3), img_path['pawn']["BLACK"]), 
                        Pawn("BLACK", (1,4), img_path['pawn']["BLACK"]), Pawn("BLACK", (1,5), img_path['pawn']["BLACK"]), 
                        Pawn("BLACK", (1,6), img_path['pawn']["BLACK"]), Pawn("BLACK", (1,7), img_path['pawn']["BLACK"])],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [Pawn("WHITE", (6,0), img_path['pawn']['WHITE']), Pawn("WHITE", (6,1), img_path['pawn']['WHITE']), 
                        Pawn("WHITE", (6,2), img_path['pawn']['WHITE']), Pawn("WHITE", (6,3), img_path['pawn']['WHITE']), 
                        Pawn("WHITE", (6,4), img_path['pawn']['WHITE']), Pawn("WHITE", (6,5), img_path['pawn']['WHITE']), 
                        Pawn("WHITE", (6,6), img_path['pawn']['WHITE']), Pawn("WHITE", (6,7), img_path['pawn']['WHITE'])],
                       [Rook("WHITE", (7,0), img_path['rook']['WHITE']), Knight("WHITE", (7,1), img_path['knight']['WHITE']), 
                        Bishop("WHITE", (7,2), img_path['bishop']['WHITE']), Queen("WHITE", (7,3), img_path['queen']['WHITE']), 
                        King("WHITE", (7,4), img_path['king']['WHITE']), Bishop("WHITE", (7,5), img_path['bishop']['WHITE']), 
                        Knight("WHITE", (7,6), img_path['knight']['WHITE']), Rook("WHITE", (7,7), img_path['rook']['WHITE'])] ]
        