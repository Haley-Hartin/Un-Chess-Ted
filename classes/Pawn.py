from classes.Piece import Piece
from classes.Queen import Queen

class Pawn(Piece):
    def create(self, id,  color, position):
        self.id = id
        self.type = "Pawn"
        self.color = color
        self.position = position
        self.isCaptured = False
        #print("Creating " + self.color + " " + self.type)

    def getID(self):
        return self.id

    def giveMoveList(self, board):
        moveList = []


        possible_column = self.position[1] # The column in which the pawn can move

        if(self.getColor() == "white"):

            # The white pawn has moved all the way to the last row and cannot move any more
            if(self.position[0] == 7):
                print("Update white pawn to queen")
                return moveList

            # The white pawn has moved before and can only move forward one position
            elif(self.position[0] <= 6 and self.position[0] > 1):
                possible_row_1 = self.position[0] + 1
                if (board.getPiece(possible_row_1,possible_column) is None):  # If one space in front of the pawn is empty is can move there
                    moveList.append([possible_row_1, possible_column])
                return moveList

            # The white pawn has not moved before and can move forward one or two spaces if they are empty
            elif(self.position[0] == 1):
                possible_row_1 = self.position[0] + 1
                possible_row_2 = self.position[0] + 2
                if (board.getPiece(possible_row_1,possible_column) is None):  # If one space in front of the pawn is empty is can move there
                    moveList.append([possible_row_1, possible_column])
                    if (board.getPiece(possible_row_2,possible_column) is None):  # If one space in front of the pawn is empty and the second one is empty as well it can move there
                        moveList.append([possible_row_2, possible_column])
                return moveList

        elif(self.getColor() == "black"):

            # The black pawn has moved all the way to the first row and cannot move any more
            if (self.position[0] == 0):
                print("Update black pawn to queen")
                return moveList

            # The black pawn has moved before and can only move forward one position
            elif (self.position[0] >= 1 and self.position[0] < 6):
                possible_row_1 = self.position[0] - 1
                if (board.getPiece(possible_row_1,possible_column) is None):  # If one space in front of the pawn is empty is can move there
                    moveList.append([possible_row_1, possible_column])
                return moveList

            # The black pawn has not moved before and can move forward one or two spaces if they are empty
            elif (self.position[0] == 6):
                possible_row_1 = self.position[0] - 1
                possible_row_2 = self.position[0] - 2
                if (board.getPiece(possible_row_1,possible_column) is None):  # If one space in front of the pawn is empty is can move there
                    moveList.append([possible_row_1, possible_column])
                    if (board.getPiece(possible_row_2,possible_column) is None):  # If one space in front of the pawn is empty and the second one is empty as well it can move there
                        moveList.append([possible_row_2, possible_column])
                return moveList



    def giveCaptureList(self,board):

        captureList = []

        if (self.getColor() == "white"):

            if (self.position[0] == 7):
                return captureList

            possible_row = self.position[0] + 1

            # The white pawn is in the first column and can only capture pieces that are in the column to its right
            if(self.position[1] == 0):
                possible_column_1 = 1
                if(board.getPiece(possible_row,possible_column_1) is not None and board.getPiece(possible_row,possible_column_1).getColor() == "black"):
                    captureList.append([possible_row, possible_column_1])
                return captureList

            # The white pawn is in the last column and can only capture pieces that are in the column to its left
            elif(self.position[1] == 7):
                possible_column_1 = 6
                if (board.getPiece(possible_row, possible_column_1) is not None and board.getPiece(possible_row, possible_column_1).getColor() == "black"):
                    captureList.append([possible_row, possible_column_1])
                return captureList

            else:

                possible_column_1 = self.position[1] - 1
                possible_column_2 = self.position[1] + 1
                if (board.getPiece(possible_row, possible_column_1) != None and board.getPiece(possible_row, possible_column_1).getColor() == "black"):

                    captureList.append([possible_row, possible_column_1])
                if (board.getPiece(possible_row, possible_column_2) != None and board.getPiece(possible_row, possible_column_2).getColor() == "black"):

                    captureList.append([possible_row, possible_column_2])
                return captureList

        elif(self.getColor() == "black"):

            if (self.position[0] == 0):
                return captureList

            possible_row = self.position[0] - 1

            # The black pawn is in the first column and can only capture pieces that are in the column to its right
            if (self.position[1] == 0):
                possible_column_1 = 1
                if (board.getPiece(possible_row, possible_column_1) != None and board.getPiece(possible_row, possible_column_1).getColor() == "white"):
                    captureList.append([possible_row, possible_column_1])
                return captureList

            # The black pawn is in the last column and can only capture pieces that are in the column to its left
            elif (self.position[1] == 7):
                possible_column_1 = 6
                if (board.getPiece(possible_row, possible_column_1) != None and board.getPiece(possible_row, possible_column_1).getColor() == "white"):
                    captureList.append([possible_row, possible_column_1])
                return captureList

            else:
                possible_column_1 = self.position[1] - 1
                possible_column_2 = self.position[1] + 1
                if (board.getPiece(possible_row, possible_column_1) != None and board.getPiece(possible_row, possible_column_1).getColor() == "white"):

                    captureList.append([possible_row, possible_column_1])
                if (board.getPiece(possible_row, possible_column_2) != None and board.getPiece(possible_row, possible_column_2).getColor() == "white"):

                    captureList.append([possible_row, possible_column_2])
                return captureList
    #check whether a black or white piece is on the opposite side of the board, enabling it to be promoted
    def able_to_promote(self):
        if(self.getColor() == "white" and self.position[0] == 7):
            return True
        if(self.getColor() == "black" and self.position[0] == 0):
            return True
        return False

    #promotes the pawn to a Queen, with all of the same properties, except with a "Q" added to the end ID to indicate a promoted pawn
    def promotion(self):
        queen_to_return = Queen()
        queen_to_return.create(self.getID() + "Q", self.getColor(), self.position)
        return queen_to_return
