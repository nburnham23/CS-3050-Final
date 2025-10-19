from Piece import Piece
from Pawn import Pawn
from Bishop import Bishop
from Knight import Knight
from Rook import Rook
from Queen import Queen
from King import King

# Dictionary for pieces' image paths
img_path = {
    'pawn': {
        'BLACK': 'pieceimages/black_pawn.png',
        'WHITE': 'pieceimages/white_pawn.png'
    },
    'knight': {
        'BLACK': 'pieceimages/black_knight.png',
        'WHITE': 'pieceimages/white_knight.png'
    },
    'bishop': {
        'BLACK': 'pieceimages/black_bishop.png',
        'WHITE': 'pieceimages/white_bishop.png'
    },
    'rook': {
        'BLACK': 'pieceimages/black_rook.png',
        'WHITE': 'pieceimages/white_rook.png'
    },
    'queen': {
        'BLACK': 'pieceimages/black_queen.png',
        'WHITE': 'pieceimages/white_queen.png'
    },
    'king': {
        'BLACK': 'pieceimages/black_king.png',
        'WHITE': 'pieceimages/white_king.png'
    }
}

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
        
        move_start = None
        move_end = None
        
        white_taken = []
        black_taken = []
    
    def get_piece(self, board_position):
        row, col = board_position
        return self.board[row][col]
    
    def set_piece(self, board_position, piece):
        row, col = board_position
        self.board[row][col] = piece
    
    # Check if move is valid, then update board and piece's moveset
    def move(self, piece_position, new_position):
        piece = self.get_piece(piece_position)
        if piece is None:
            return False

        # Validate move
        # if new_position not in piece.move():
        if new_position not in piece.moveset:
            return False
        
        # # Check if enemy piece is in spot, and if so add to taken list
        # enemy_piece = self.get_piece(new_position)
        # if enemy_piece:
        #     if enemy_piece.piece_color == 'BLACK':
        #         self.black_taken.append(enemy_piece)
        #     else:
        #         self.white_taken.append(enemy_piece)
        
        # Update pieces information
        piece.board_position = new_position
        piece.set_sprite_position(5, 80, 80)
        piece.calculate_moves()

        # Make move on board
        self.set_piece(new_position, piece)
        self.set_piece(piece_position, None)

        return True
    
    # toString method
    def display(self):
        print(self.board)