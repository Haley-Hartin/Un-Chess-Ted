from __future__ import annotations
from classes.PieceFactory import PieceFactory
from classes.Observer import Observer
from classes.Player import Player
from abc import ABC, abstractmethod
from copy import deepcopy

class ChessBoard:
    def __init__(self):
        self.board = {}
        self.populate_chess_board()

    def populate_chess_board(self):
        print()
        print("Creating chess board")
        print()
        piece_factory = PieceFactory()

        for x in range(0,8):
            for y in range(0,8):
                key = "(" + str(x) + ", " + str(y) + ")"
                self.board[key] = None

        # Create Pawns
        for i in range(0,8):
            w = "wP" + str(i+1)
            b = "bP" + str(i+1)
            w_key = "(1, " + str(i) + ")"
            b_key = "(6, " + str(i) + ")"
            self.board[w_key] = piece_factory.createPiece(w, "Pawn", "white", [1, i])
            self.board[b_key] = piece_factory.createPiece(b, "Pawn", "black", [6, i])

        # Create Bishops
        self.board['(0, 2)'] = piece_factory.createPiece("wB1", "Bishop", "white", [0, 2])
        self.board['(0, 5)'] = piece_factory.createPiece("wB2", "Bishop", "white", [0, 5])
        self.board['(7, 2)'] = piece_factory.createPiece("bB1", "Bishop", "black", [7, 2])
        self.board['(7, 5)'] = piece_factory.createPiece("bB2", "Bishop", "black", [7, 5])

        # Create Knights
        self.board['(0, 1)'] = piece_factory.createPiece("wN1", "Knight", "white", [0, 1])
        self.board['(0, 6)'] = piece_factory.createPiece("wN2", "Knight", "white", [0, 6])
        self.board['(7, 1)'] = piece_factory.createPiece("bN1", "Knight", "black", [7, 1])
        self.board['(7, 6)'] = piece_factory.createPiece("bN2", "Knight", "black", [7, 6])

        # Create Rooks
        self.board['(0, 0)'] = piece_factory.createPiece("wR1", "Rook", "white", [0, 0])
        self.board['(0, 7)'] = piece_factory.createPiece("wR2", "Rook", "white", [0, 7])
        self.board['(7, 0)'] = piece_factory.createPiece("bR1", "Rook", "black", [7, 0])
        self.board['(7, 7)'] = piece_factory.createPiece("bR2", "Rook", "black", [7, 7])

        # Create Queens
        self.board['(0, 3)'] = piece_factory.createPiece("wQ1", "Queen", "white", [0, 3])
        self.board['(7, 3)'] = piece_factory.createPiece("bQ2", "Queen", "black", [7, 3])


        # Create Kings
        self.board['(0, 4)'] = piece_factory.createPiece("wK1", "King", "white", [0, 4])
        self.board['(7, 4)'] = piece_factory.createPiece("bK2", "King", "black", [7, 4])

        self.print_board()

    def print_board(self):
        # Print out the chess board to the console
        for x in range(7,-1,-1):
            for y in range(8):
                key = "(" + str(x) + ", " + str(y) + ")"
                if(self.board[key] == None):
                    print("--- ", end="")
                else:
                    print(self.board[key].getId() + " ", end="")
            print()

        print()

    def getBoard(self):
        return self.board

    def getMoveListForPiece(self,row,column,color):
        piece = self.board[str((row, column))]
        list = piece.getList(self)
        return list


    # Function to return the piece that is at the given location - If location empty returns None
    def getPiece(self, row, column):
        x = str((row, column))
        if (self.board[x] != None):
            return self.board[x]
        else:
            return None

    # Function to return the piece color that is at the given location - If location is empty return None
    def getPieceColor(self,row,column):
        x = str((row, column))
        if(self.board[x] != None):
            color = self.board[x].getColor()
            return color
        else:
            #print("There is no piece at that location -- cannot return color")
            return None

    #get's all of the locations of the black pieces on the board into a list
    def getBlackPieceLocations(self):
        locations = []
        for location in self.board:
            if(self.board[location] != None):
                if(self.board[location].getColor() == "black"):
                    locations.append(self.board[location].getPosition())

        return locations

    #moves a piece on the board at the initial lcoation and final loctation's specified
    def updateBoard(self, initialRow, initialColumn, finalRow, finalColumn):
        initialLocation = str((initialRow, initialColumn))
        finalLocation = str((finalRow,finalColumn))

        # If the final location of the piece is not empty then it is capturing -- set the piece at that location to be captured
        if(self.board[finalLocation] != None):
            self.board[finalLocation].setIsCaptured(True)
        newPostion = [finalRow, finalColumn]
        self.board[initialLocation].setPosition(newPostion)
        self.board[finalLocation] = self.board[initialLocation]
        self.board[initialLocation] = None
        #see if the piece is a pawn that is able to be promoted
        if(self.board[finalLocation].getPieceType() == "Pawn" and self.board[finalLocation].able_to_promote() == True):
            self.board[finalLocation] = self.board[finalLocation].promotion() #promote the pawn to a queen

    def check_stalemate(self, player_color):
        #loop through the board
        for x in range(0,8):
            for y in range(0,8):
                piece_color = self.getPieceColor(x,y)
                if piece_color != None:
                    #check each piece of the player in question
                    if piece_color == player_color:
                        moves = self.getMoveListForPiece(x,y,piece_color)
                        if moves != None:
#                             print("The game is not over.")
                            return False #check if theres any possible moves
#         print("The game is at stalemate.")
        return True



    def find_piece_location(self, piece_id):

        #find the location of a piece on the board
        for x in range(0,8):
            for y in range(0,8):
                piece =  self.getPiece(x,y)
                if piece:
                    if piece.getID() == piece_id:
                        return x,y
        return None


    def king_is_in_check(self, color, king_location):
        #loop through the board
        for x in range(0,8):
            for y in range(0,8):
                #check the color of each piece
                piece_color = self.getPieceColor(x,y)
                if piece_color != None:

                    #If its the other players piece
                    if piece_color != color:

                        #get the pieces moves
                        moves = self.getMoveListForPiece(x,y,piece_color)
                        piece = self.getPiece(x,y)
#                         print(king_location, moves, piece.getPosition())
                        if king_location in moves: #if the piece can move to the king
#                             print("The ", color, " king IS in check by ", piece.getPosition())
#                             print(king_location, moves, piece.getID())
                            return True #check if theres any possible moves
#         print("The king is NOT in check.")
        return False

    def clone(self): #https://docs.python.org/3/library/copy.html
        return deepcopy(self) #prototype pattern - creates a new object identical to the state of the current object
