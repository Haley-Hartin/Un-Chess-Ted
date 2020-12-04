from classes.Rook import Rook
from classes.Pawn import Pawn
from classes.Bishop import Bishop
from classes.Knight import Knight
from classes.Queen import Queen
from classes.King import King
from classes.Piece import Piece


#Pattern - Simple Factory Pattern
class PieceFactory(object):
    @classmethod
    def createPiece(cls, id, piece_name, color, position) -> Piece: #https://aaravtech.medium.com/design-patterns-in-python-factory-c728b88603eb
        new_piece = eval(piece_name)()
        new_piece.create(id, color, position)
        return new_piece
