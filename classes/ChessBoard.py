from __future__ import annotations
from classes.PieceFactory import PieceFactory
from classes.Observer import Observer
from classes.Player import Player
from abc import ABC, abstractmethod

class ChessBoard:
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

    def convertList(self, finalList):
        stringList = []
        file = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for pair in finalList:
            position = file[pair[1]] + str(pair[0] + 1 )
            stringList.append(position)
        return stringList


    def getMoveListForPiece(self,row,column,color):
        piece = self.board[str((row, column))]
        moveList = piece.giveMoveList(self)
        print("The move list is: ")
        print(moveList)
        captureList = piece.giveCaptureList(self)
        print("The capture list is: ")
        print(captureList)
        if(moveList != None and captureList != None):
            finalList = moveList + captureList
        elif(moveList != None and captureList == None):
            finalList = moveList
        elif (moveList == None and captureList != None):
            finalList = captureList
        else:
            return None
        print(finalList)
        convertedList = self.convertList(finalList)
        print("The piece is allowed to move to: ")
        print(convertedList)
        return convertedList


    def getPiece(self, row, column):
        x = str((row, column))
        if (self.board[x] != None):
            return self.board[x]
        else:
            return None 

    def getPieceColor(self,row,column):
        x = str((row, column))
        if(self.board[x] != None):
            color = self.board[x].getColor()
            return color
        else:
            #print("There is no piece at that location -- cannot return color")
            return None


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
                            print("The game is not over.")
                            return False #check if theres any possible moves
        print("The game is at stalemate.")
        return True 
    
    def check_checkmate(self, color):
        print("checking if " + color + " is in checkmate.")
        for x in range(0,8):
            for y in range(0,8):
                if ((self.getPieceColor(x,y)==color) and (self.getPiece(x,y) == 'wK1' or self.getPiece(x,y) == 'bK2') ):
                    king = self.getPiece(x,y)
                    if king.is_captured() and self.getMoveListForPiece(x,y,color):
                        print(color + "'s king is in checkmate with no moves.")
                        return True
        print(color + "'s king is not in checkmate with no moves.")
        return False
         
                
                        
                            



