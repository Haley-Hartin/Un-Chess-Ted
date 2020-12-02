from classes.Piece import Piece

class King(Piece):
    def create(self, id,  color, position):
        self.id = id
        self.type = "King"
        self.color = color
        self.position = position
        self.isCaptured = False

    def getID(self):
        return self.id
    
    def getPosition(self):
        return self.position

    def giveMoveList(self, board):
        moveList = []

        row = self.position[0]
        column = self.position[1]
        if(row + 1 <= 7):
            if(column - 1 >= 0):
                if (board.getPiece(row + 1, column - 1) == None):
                    moveList.append([row + 1, column -1])
            if (board.getPiece(row + 1, column) == None):
                moveList.append([row + 1, column])
            if (column + 1 <= 7):
                if (board.getPiece(row + 1, column + 1) == None):
                    moveList.append([row + 1, column + 1])

        if (row - 1 >= 0):
            if (column - 1 >= 0):
                if (board.getPiece(row - 1, column - 1) == None):
                    moveList.append([row - 1, column -1])
            if (board.getPiece(row - 1, column) == None):
                moveList.append([row - 1, column])
            if (column + 1 <= 7):
                if (board.getPiece(row - 1, column + 1) == None):
                    moveList.append([row - 1, column + 1])

        if(column - 1 >= 0):
            if (board.getPiece(row, column - 1) == None):
                moveList.append([row, column - 1])
        if (column + 1 <= 7):
            if (board.getPiece(row, column + 1) == None):
                moveList.append([row, column + 1])

        return moveList


    def giveCaptureList(self,board):
        captureList = []

        row = self.position[0]
        column = self.position[1]

        if (row + 1 <= 7):
            if (column - 1 >= 0):
                if (board.getPiece(row + 1, column - 1) != None and board.getPiece(row + 1, column - 1).getColor() != self.color):
                    captureList.append([row + 1, column - 1])
            if (board.getPiece(row + 1, column) != None and board.getPiece(row + 1, column).getColor() != self.color):
                captureList.append([row + 1, column])
            if (column + 1 <= 7):
                if (board.getPiece(row + 1, column + 1) != None and board.getPiece(row + 1, column + 1).getColor() != self.color):
                    captureList.append([row + 1, column + 1])

        if (row - 1 >= 0):
            if (column - 1 >= 0):
                if (board.getPiece(row - 1, column - 1) != None and board.getPiece(row - 1, column - 1).getColor() != self.color):
                    captureList.append([row - 1, column - 1])
            if (board.getPiece(row - 1, column) != None and board.getPiece(row - 1, column).getColor() != self.color):
                captureList.append([row - 1, column])
            if (column + 1 <= 7):
                if (board.getPiece(row - 1, column + 1) != None and board.getPiece(row - 1, column + 1).getColor() != self.color):
                    captureList.append([row - 1, column + 1])

        if (column - 1 >= 0):
            if (board.getPiece(row, column - 1) != None and board.getPiece(row, column - 1).getColor() != self.color):
                captureList.append([row, column - 1])
        if (column + 1 <= 7):
            if (board.getPiece(row, column + 1) != None and board.getPiece(row, column + 1).getColor() != self.color):
                captureList.append([row, column + 1])

        return captureList
    
    def is_captured(self):
        return self.isCaptured
    

        