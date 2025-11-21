"""
Board class
"""
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

class Board:
    """Board class"""
    def __init__(self):
        self.black_taken = []
        self.white_taken = []

        self.board = [ [Rook("WHITE", (0,0), img_path['rook']["WHITE"]),
                        Knight("WHITE", (0,1), img_path['knight']["WHITE"]),
                        Bishop("WHITE", (0,2), img_path['bishop']["WHITE"]),
                        Queen("WHITE", (0,3), img_path['queen']["WHITE"]),
                        King("WHITE", (0,4), img_path['king']["WHITE"]),
                        Bishop("WHITE", (0,5), img_path['bishop']["WHITE"]),
                        Knight("WHITE", (0,6), img_path['knight']["WHITE"]),
                        Rook("WHITE", (0,7), img_path['rook']["WHITE"])],
                       [Pawn("WHITE", (1,0), img_path['pawn']["WHITE"]),
                        Pawn("WHITE", (1,1), img_path['pawn']["WHITE"]),
                        Pawn("WHITE", (1,2), img_path['pawn']["WHITE"]),
                        Pawn("WHITE", (1,3), img_path['pawn']["WHITE"]),
                        Pawn("WHITE", (1,4), img_path['pawn']["WHITE"]),
                        Pawn("WHITE", (1,5), img_path['pawn']["WHITE"]),
                        Pawn("WHITE", (1,6), img_path['pawn']["WHITE"]),
                        Pawn("WHITE", (1,7), img_path['pawn']["WHITE"])],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [Pawn("BLACK", (6,0), img_path['pawn']['BLACK']),
                        Pawn("BLACK", (6,1), img_path['pawn']['BLACK']),
                        Pawn("BLACK", (6,2), img_path['pawn']['BLACK']),
                        Pawn("BLACK", (6,3), img_path['pawn']['BLACK']),
                        Pawn("BLACK", (6,4), img_path['pawn']['BLACK']),
                        Pawn("BLACK", (6,5), img_path['pawn']['BLACK']),
                        Pawn("BLACK", (6,6), img_path['pawn']['BLACK']),
                        Pawn("BLACK", (6,7), img_path['pawn']['BLACK'])],
                       [Rook("BLACK", (7,0), img_path['rook']['BLACK']),
                        Knight("BLACK", (7,1), img_path['knight']['BLACK']),
                        Bishop("BLACK", (7,2), img_path['bishop']['BLACK']),
                        Queen("BLACK", (7,3), img_path['queen']['BLACK']),
                        King("BLACK", (7,4), img_path['king']['BLACK']),
                        Bishop("BLACK", (7,5), img_path['bishop']['BLACK']),
                        Knight("BLACK", (7,6), img_path['knight']['BLACK']),
                        Rook("BLACK", (7,7), img_path['rook']['BLACK'])] ]

        # initialize movesets for all pieces
        self.calculate_movesets()

    def get_piece(self, board_position):
        row, col = board_position
        return self.board[row][col]

    def set_piece(self, board_position, piece):
        row, col = board_position
        self.board[row][col] = piece

    # Updates all pieces' movesets
    def calculate_movesets(self):
        for row in self.board:
            for piece in row:
                if piece:
                    piece.calculate_moves(self)


    # Check if move is valid, then update board and piece's moveset
    def move(self, piece_position, new_position):
        piece = self.get_piece(piece_position)
        if piece is None:
            print("Piece does not exist")
            return False

        # Validate move
        # if new_position not in piece.move():
        if new_position not in piece.moveset:
            print("Move not in moveset")
            return False

        captured_piece = self.get_piece(new_position)
        if captured_piece and captured_piece.piece_color == 'BLACK':
            self.black_taken.append(captured_piece)
        elif captured_piece and captured_piece.piece_color == 'WHITE':
            self.white_taken.append(captured_piece)

        # Update pieces information
        piece.curr_position = new_position

        # Make move on board
        self.set_piece(new_position, piece)
        self.set_piece(piece_position, None)

        # Update if pawn has moved
        if isinstance(piece, Pawn):
            piece.has_moved = True

        # Update board state
        self.calculate_movesets()

        return True

    # toString method
    def display(self):
        print(self.board)
