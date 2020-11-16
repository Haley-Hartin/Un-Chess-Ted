from abc import ABC, abstractmethod #https://www.python-course.eu/python3_abstract_classes.php
import pieces

class Player(ABC):
    __init__(self, name):
        self.name = name #https://www.python-course.eu/python3_inheritance.php

    @abstractmethod
    def makeMove():
        pass

class HumanPlayer(Player):

    def makeMove():
        print("makeMove")


class ChessGame:
    __init__(self, p1_name, p2_name, game_type):
        self.white = HumanPlayer(p1_name)
        if(p2_type == "Multiplayer"):
            self.black = HumanPlayer(p2_name)
        self.board = ChessBoard()
    def getPlayersPiece():
        pass
    def changePlayer():
        pass

class ChessBoard:
    __init__(self):
        files = ["A", "B", "C", "D", "E", "F","G", "H"]
        ranks = [1,2,3,4,5,6,7,8]
        self.pieces = {}
        for f in files:
            for r in ranks:
                if(f not in self.pieces):
                    self.pieces[f] = {}
                if(r not in self.pieces[f]):
                    self.pieces[f][r] = None

        presetBoard = {'A7' : ("black", "pawn"), 'B7' : ("black", "pawn"), 'C7' : ("black", "pawn"), 'D7' : ("black", "pawn"), 'E7' : ("black", "pawn"), 'F7' : ("black", "pawn"), 'G7' : ("black", "pawn"), 'H7' : ("black", "pawn"),
        'A2': ("white", "pawn"), 'B2': ("white", "pawn"), 'C2': ("white", "pawn"), 'D2': ("white", "pawn"), 'E2': ("white", "pawn"), 'F2': ("white", "pawn"), 'G2': ("white", "pawn"), 'H2':("white", "pawn"),
        'A8':("black","rook"), 'H8': ("black","rook"), 'A1': ("white", "rook"), 'H1': ("white", "rook"),
        'B8': ("black", "knight"), 'G8': ("black", "knight"), 'B1': ("white", "knight"), 'G1': ("white", "knight"),
        'C8':("black", "bishop"), 'F8':("black", "bishop"), 'C1': ("white", "bishop"), 'F1': ("white", "bishop"),
        'D8':("black", "queen"), 'D1': ("white", "queen"), 'E1': ("white", "king"), 'E8': ("black", "king") }

        self.pieceFactory = PieceFactory()

        for pos in presetBoard:
            file = pos[0]
            rank = pos[1]
            piece = presetBoard[pos]
            self.pieces[file][rank] = pieceFactory.createPiece(piece[0], piece[1])


    def movePiece(self, file, rank):
        pass
    def clone():
        pass
