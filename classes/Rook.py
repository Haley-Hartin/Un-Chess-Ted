from classes.Piece import Piece

class Rook(Piece):
    def create(self, id, color, position):
        self.id = id
        self.type = "Rook"
        self.color = color
        self.position = position
        self.isCaptured = False


    def getID(self):
        return self.id

    def giveMoveList(self, board):
        moveList = []

        row = self.position[0] + 1 # one row above the rook's current spot
        column = self.position[1] # The rook's current column
        blocked = False

        # Check all spaces that are in the same column and above the rook until it is blocked by another piece
        while(row <= 7 and blocked == False):
            if(board.getPiece(row, column) == None):
                moveList.append([row, column])
            else:
                blocked = True
            row = row + 1

        row = self.position[0] - 1 # one row below the rook's current spot
        column = self.position[1] # The rook's current column
        blocked = False

        # Check all spaces that are in the same column and below the rook until it is blocked by another piece
        while(row >= 0 and blocked == False):
            if (board.getPiece(row, column) == None):
                moveList.append([row, column])
            else:
                blocked = True
            row = row - 1

        row = self.position[0] # The rooks current row
        column = self.position[1] + 1 # One space to the right of the rook
        blocked = False

        # Check all spaces that are in the same row and to the right of the rook until it is blocked by another piece
        while (column <= 7 and blocked == False):
            if (board.getPiece(row, column) == None):
                moveList.append([row, column])
            else:
                blocked = True
            column = column + 1

        row = self.position[0] # The rook's current row
        column = self.position[1] - 1 # One space to the left of the rook
        blocked = False

        # Check all spaces that are in the same row and to the left of the rook until it is blocked by another piece
        while (column >= 0 and blocked == False):
            if (board.getPiece(row, column) == None):
                moveList.append([row, column])
            else:
                blocked = True
            column = column - 1

        return moveList


    def giveCaptureList(self,board):
        captureList = []

        row = self.position[0] + 1 # One row above the rooks current spot
        column = self.position[1] # The rooks current column
        blocked = False

        # Check all spaces that are in the same column and above the rook until it is blocked by its own color piece or can capture an any piece
        while (row <= 7 and blocked == False):
            if (board.getPiece(row, column) != None and board.getPiece(row, column).getColor() != self.color):
                captureList.append([row, column])
                blocked = True
            elif (board.getPiece(row, column) != None and board.getPiece(row, column).getColor() == self.color):
                blocked = True
            row = row + 1

        row = self.position[0] - 1 # One row below the rook's current spot
        column = self.position[1] # The rooks current column
        blocked = False

        # Check all spaces that are in the same column and below the rook until it is blocked by its own color piece or can capture an any piece
        while (row >= 0 and blocked == False):
            if (board.getPiece(row, column) != None and board.getPiece(row, column).getColor() != self.color):
                captureList.append([row, column])
                blocked = True
            elif (board.getPiece(row, column) != None and board.getPiece(row, column).getColor() == self.color):
                blocked = True
            row = row - 1

        row = self.position[0] # The rooks current row
        column = self.position[1] + 1 # One spot to the right of the Rook
        blocked = False

        # Check all spaces that are in the same crow and to the right of the rook until it is blocked by its own color piece or can capture an enemy piece
        while (column <= 7 and blocked == False):
            if (board.getPiece(row, column) != None and board.getPiece(row, column).getColor() != self.color):
                captureList.append([row, column])
                blocked = True
            elif (board.getPiece(row, column) != None and board.getPiece(row, column).getColor() == self.color):
                blocked = True
            column = column + 1

        row = self.position[0] # The rooks current row
        column = self.position[1] - 1 # One spot to the left of the Rook
        blocked = False

        # Check all spaces that are in the same crow and to the left of the rook until it is blocked by its own color piece or can capture an enemy piece
        while (column >= 0 and blocked == False):
            if (board.getPiece(row, column) != None and board.getPiece(row, column).getColor() != self.color):
                captureList.append([row, column])
                blocked = True
            elif (board.getPiece(row, column) != None and board.getPiece(row, column).getColor() == self.color):
                blocked = True
            column = column - 1

        return captureList