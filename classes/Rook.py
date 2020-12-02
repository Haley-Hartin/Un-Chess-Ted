from classes.Piece import Piece

class Rook(Piece):
    def create(self, id, color, position):
        self.id = id
        self.type = "Rook"
        self.color = color
        self.position = position
        self.isCaptured = False
        #print("Creating " + self.color + " " + self.type)

    def getID(self):
        return self.id

    def giveMoveList(self, board):
        moveList = []

        row = self.position[0] + 1
        column = self.position[1]
        blocked = False

        while(row <= 7 and blocked == False):
            print("First While Loop")
            if(board.getPiece(row, column) == None):
                moveList.append([row, column])
            else:
                blocked = True
            row = row + 1

        row = self.position[0] - 1
        column = self.position[1]
        blocked = False

        while(row >= 0 and blocked == False):
            print("Second While Loop")
            if (board.getPiece(row, column) == None):
                moveList.append([row, column])
            else:
                blocked = True
            row = row - 1

        row = self.position[0]
        column = self.position[1] + 1
        blocked = False

        while (column <= 7 and blocked == False):
            print("Third While Loop")
            if (board.getPiece(row, column) == None):
                moveList.append([row, column])
            else:
                blocked = True
            column = column + 1

        row = self.position[0]
        column = self.position[1] - 1
        blocked = False

        while (column >= 0 and blocked == False):
            print("Fourth While Loop")
            if (board.getPiece(row, column) == None):
                moveList.append([row, column])
            else:
                blocked = True
            column = column - 1

        return moveList


    def giveCaptureList(self,board):
        print("Getting Rook Move List")
        captureList = []

        row = self.position[0] + 1
        column = self.position[1]
        blocked = False

        while (row <= 7 and blocked == False):
            print("First While Loop")
            if (board.getPiece(row, column) != None and board.getPiece(row, column).getColor() != self.color):
                captureList.append([row, column])
                blocked = True
            elif (board.getPiece(row, column) != None and board.getPiece(row, column).getColor() == self.color):
                blocked = True
            row = row + 1

        row = self.position[0] - 1
        column = self.position[1]
        blocked = False

        while (row >= 0 and blocked == False):
            print("Second While Loop")
            if (board.getPiece(row, column) != None and board.getPiece(row, column).getColor() != self.color):
                captureList.append([row, column])
                blocked = True
            elif (board.getPiece(row, column) != None and board.getPiece(row, column).getColor() == self.color):
                blocked = True
            row = row - 1

        row = self.position[0]
        column = self.position[1] + 1
        blocked = False

        while (column <= 7 and blocked == False):
            print("Third While Loop")
            if (board.getPiece(row, column) != None and board.getPiece(row, column).getColor() != self.color):
                captureList.append([row, column])
                blocked = True
            elif (board.getPiece(row, column) != None and board.getPiece(row, column).getColor() == self.color):
                blocked = True
            column = column + 1

        row = self.position[0]
        column = self.position[1] - 1
        blocked = False

        while (column >= 0 and blocked == False):
            print("Fourth While Loop")
            if (board.getPiece(row, column) != None and board.getPiece(row, column).getColor() != self.color):
                captureList.append([row, column])
                blocked = True
            elif (board.getPiece(row, column) != None and board.getPiece(row, column).getColor() == self.color):
                blocked = True
            column = column - 1

        return captureList