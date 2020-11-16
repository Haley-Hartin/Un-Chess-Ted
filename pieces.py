from abc import ABC, abstractmethod #https://www.python-course.eu/python3_abstract_classes.php

class PieceFactory:
    def createPiece(self, color, type):
        if(type == "pawn"):
            return Pawn(color)
        elif(type == "rook"):
            return Rook(color)
        elif(type == "bishop"):
            return Bishop(color)
        elif(type == "knight"):
            reuturn Knight(color)
        elif(type == "queen"):
            return Queen(color)
        elif(type == "king"):
            return King(color)

        return None

class Piece(ABC):
    __init__(self,color):
        self.color = color

    @abstractmethod
    def turn():
        pass

class Bishop(Piece):

class King(Piece):

class Knight(Piece):

class Pawn(Piece):

class Queen(Piece):

class Rook(Piece):
