from classes.Piece import Piece

class Knight(Piece):
    def create(self, id,  color, position):
        self.id = id
        self.type = "Knight"
        self.color = color
        self.position = position
        self.isCaptured = False
        #print("Creating " + self.color + " " + self.type)

    def getID(self):
        return self.id

    def giveMoveList(self, board):

        moveList = []
        row = self.position[0]
        column = self.position[1]

        #Check space above the Knight

        if(row + 2 <= 7 and column - 1 >= 0):
            if (board.getPiece(row + 2, column - 1) == None):
                moveList.append([row + 2, column -1])

        if(row + 1 <=7 and column - 2 >= 0):
            if (board.getPiece(row + 1, column - 2) == None):
                moveList.append([row + 1, column -2])

        if (row + 1 <= 7 and column + 2 <= 7):
            if (board.getPiece(row + 1, column + 2) == None):
                moveList.append([row + 1, column + 2])

        if (row + 2 <= 7 and column + 1 <= 7):
            if (board.getPiece(row + 2, column + 1) == None):
                moveList.append([row + 2, column + 1])

        # Check spaces below the Knight

        if (row - 1 >= 0 and column - 2 >= 0):
            if (board.getPiece(row - 1, column - 2) == None):
                moveList.append([row - 1, column - 2])

        if (row - 2 >= 0 and column - 1 >= 0):
            if (board.getPiece(row - 2, column - 1) == None):
                moveList.append([row - 2, column - 1])

        if (row - 1 >= 0 and column + 2 <= 7):
            if (board.getPiece(row - 1, column + 2) == None):
                moveList.append([row - 1, column + 2])

        if (row - 2 >= 0 and column + 1 <= 7):
            if (board.getPiece(row - 2, column + 1) == None):
                moveList.append([row - 2, column + 1])

        return moveList


    def giveCaptureList(self,board):
        captureList = []
        row = self.position[0]
        column = self.position[1]

        # Check space above the Knight

        if (row + 2 <= 7 and column - 1 >= 0):
            if (board.getPiece(row + 2, column - 1) != None and board.getPiece(row + 2, column - 1).getColor() != self.color):
                captureList.append([row + 2, column - 1])

        if (row + 1 <= 7 and column - 2 >= 0):
            if (board.getPiece(row + 1, column - 2) != None and board.getPiece(row + 1, column - 2).getColor() != self.color):
                captureList.append([row + 1, column - 2])

        if (row + 1 <= 7 and column + 2 <= 7):
            if (board.getPiece(row + 1, column + 2) != None and board.getPiece(row + 1, column + 2).getColor() != self.color):
                captureList.append([row + 1, column + 2])

        if (row + 2 <= 7 and column + 1 <= 7):
            if (board.getPiece(row + 2, column + 1) != None and board.getPiece(row + 2, column + 1).getColor() != self.color):
                captureList.append([row + 2, column + 1])

        # Check spaces below the Knight

        if (row - 1 >= 0 and column - 2 >= 0):
            if (board.getPiece(row - 1, column - 2) != None and board.getPiece(row - 1, column - 2).getColor() != self.color):
                captureList.append([row - 1, column - 2])

        if (row - 2 >= 0 and column - 1 >= 0):
            if (board.getPiece(row - 2, column - 1) != None and board.getPiece(row - 2, column - 1).getColor() != self.color):
                captureList.append([row - 2, column - 1])

        if (row - 1 >= 0 and column + 2 <= 7):
            if (board.getPiece(row - 1, column + 2) != None and board.getPiece(row - 1, column  + 2).getColor() != self.color):
                captureList.append([row - 1, column + 2])

        if (row - 2 >= 0 and column + 1 <= 7):
            if (board.getPiece(row - 2, column + 1) != None and board.getPiece(row - 2, column + 1).getColor() != self.color):
                captureList.append([row - 2, column + 1])

        return captureList