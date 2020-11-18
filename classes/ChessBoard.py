from __future__ import annotations
from classes.PieceFactory import PieceFactory
from classes.Observer import Observer
from classes.Player import Player
from abc import ABC, abstractmethod

class ChessBoard(Observer):
    def __init__(self):
        self.board = {}
        self.populate_chess_board()

    def populate_chess_board(self):
        print()
        print("Creating chess board")
        print()
        piece_factory = PieceFactory()
        wp1 = piece_factory.createPiece("wp1", "Pawn", "white", ["a", 8])

        for x in range(0,8):
            for y in range(0,8):
                self.board[(x,y)] = None

        # Create Pawns
        for i in range(0,8):
            w = "wP" + str(i+1)
            b = "bP" + str(i+1)
            self.board[(1, i)] = piece_factory.createPiece(w, "Pawn", "white", [1, i])
            self.board[(6, i)] = piece_factory.createPiece(b, "Pawn", "black", [6, i])

        # Create Bishops
        self.board[(0, 2)] = piece_factory.createPiece("wB1", "Bishop", "white", [0, 2])
        self.board[(0, 5)] = piece_factory.createPiece("wB2", "Bishop", "white", [0, 5])
        self.board[(7, 2)] = piece_factory.createPiece("bB1", "Bishop", "black", [7, 2])
        self.board[(7, 5)] = piece_factory.createPiece("bB2", "Bishop", "black", [7, 5])

        # Create Knights
        self.board[(0, 1)] = piece_factory.createPiece("wN1", "Knight", "white", [0, 1])
        self.board[(0, 6)] = piece_factory.createPiece("wN2", "Knight", "white", [0, 6])
        self.board[(7, 1)] = piece_factory.createPiece("bN1", "Knight", "black", [7, 1])
        self.board[(7, 6)] = piece_factory.createPiece("bN2", "Knight", "black", [7, 6])

        # Create Rooks
        self.board[(0, 0)] = piece_factory.createPiece("wR1", "Rook", "white", [0, 0])
        self.board[(0, 7)] = piece_factory.createPiece("wR2", "Rook", "white", [0, 7])
        self.board[(7, 0)] = piece_factory.createPiece("bR1", "Rook", "black", [7, 0])
        self.board[(7, 7)] = piece_factory.createPiece("bR2", "Rook", "black", [7, 7])

        # Create Queens
        self.board[(0, 3)] = piece_factory.createPiece("wQ1", "Queen", "white", [0, 3])
        self.board[(7, 3)] = piece_factory.createPiece("bQ2", "Queen", "black", [7, 3])


        # Create Kings
        self.board[(0, 4)] = piece_factory.createPiece("wK1", "King", "white", [0, 4])
        self.board[(7, 4)] = piece_factory.createPiece("bK2", "King", "black", [7, 4])

        # This is just to print the current board set up to the console
        for x in range(7,-1,-1):
            for y in range(8):
                if(self.board[(x, y)] == None):
                    print("--- ", end="")
                else:
                    print(self.board[(x, y)].getId() + " ", end="")
            print()

        print()

    def getBoard(self):
        return self.board

    def getPieceColor(self,location):
        print("I am the board and I am going to determine what color is at location " + str(location))
        # For now I am just going to return white as a default
        return "white"

    def update(self, player: Player) -> None:
        print()
        print("Board: I was just notified that the player would like to move the piece that is at location " + str(player.locationSelected) + " to location " + str(player.finalLocation))
        print("Board: I am going to update my board to reflect the players move.")

