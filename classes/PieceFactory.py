from classes.Rook import Rook
from classes.Pawn import Pawn
from classes.Bishop import Bishop
from classes.Knight import Knight
from classes.Queen import Queen
from classes.King import King
from classes.Piece import Piece


class PieceFactory(object):
    @classmethod
    def createPiece(cls, id, piece_name, color, position) -> Piece:
        new_piece = eval(piece_name)()
        new_piece.create(id, color, position)
        return new_piece
