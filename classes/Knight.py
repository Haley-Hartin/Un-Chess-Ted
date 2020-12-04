from classes.Piece import Piece

class Knight(Piece):
    def create(self, id,  color, position):
        self.id = id
        self.type = "Knight"
        self.color = color
        self.position = position
        self.isCaptured = False


    def getID(self):
        return self.id

    def giveMoveList(self, board):

        moveList = []
        row = self.position[0]
        column = self.position[1]

    # Check spaces above the Knight

        # Check space exists on the board
        if(row + 2 <= 7 and column - 1 >= 0):
            # Check space up two and left one - if empty add to move list
            if (board.getPiece(row + 2, column - 1) == None):
                moveList.append([row + 2, column -1])

        # Check space exists on the board
        if(row + 1 <=7 and column - 2 >= 0):
            # Check space up one and left two - if empty add to move list
            if (board.getPiece(row + 1, column - 2) == None):
                moveList.append([row + 1, column -2])

        # Check space exists on the board
        if (row + 1 <= 7 and column + 2 <= 7):
            # Check space up one and right two - if empty add to move list
            if (board.getPiece(row + 1, column + 2) == None):
                moveList.append([row + 1, column + 2])

        # Check space exists on the board
        if (row + 2 <= 7 and column + 1 <= 7):
            # Check space up two and right one - if empty add to move list
            if (board.getPiece(row + 2, column + 1) == None):
                moveList.append([row + 2, column + 1])

    # Check spaces below the Knight

        # Check space exists on the board
        if (row - 1 >= 0 and column - 2 >= 0):
            # Check space down one anf left two - if empty add to move list
            if (board.getPiece(row - 1, column - 2) == None):
                moveList.append([row - 1, column - 2])

        # Check space exists on the board
        if (row - 2 >= 0 and column - 1 >= 0):
            # Check space down two and left one - if empty add to move list
            if (board.getPiece(row - 2, column - 1) == None):
                moveList.append([row - 2, column - 1])

        # Check space exists on the board
        if (row - 1 >= 0 and column + 2 <= 7):
            # Check space down one and right two - if empty add to move list
            if (board.getPiece(row - 1, column + 2) == None):
                moveList.append([row - 1, column + 2])

        # Check space exists on the board
        if (row - 2 >= 0 and column + 1 <= 7):
            # Check space down two and right one - If empty add to move list
            if (board.getPiece(row - 2, column + 1) == None):
                moveList.append([row - 2, column + 1])

        return moveList


    def giveCaptureList(self,board):
        captureList = []
        row = self.position[0]
        column = self.position[1]

    # Check spaces above the Knight

        # Check space exists on the board
        if (row + 2 <= 7 and column - 1 >= 0):
            # Check space up two and left one - if enemy add to capture list
            if (board.getPiece(row + 2, column - 1) != None and board.getPiece(row + 2, column - 1).getColor() != self.color):
                captureList.append([row + 2, column - 1])

        # Check space exists on the board
        if (row + 1 <= 7 and column - 2 >= 0):
            # Check space up one and left two - if enemy add to capture list
            if (board.getPiece(row + 1, column - 2) != None and board.getPiece(row + 1, column - 2).getColor() != self.color):
                captureList.append([row + 1, column - 2])

        # Check space exists on the board
        if (row + 1 <= 7 and column + 2 <= 7):
            # Check space up one and right two - if enemy add to capture list
            if (board.getPiece(row + 1, column + 2) != None and board.getPiece(row + 1, column + 2).getColor() != self.color):
                captureList.append([row + 1, column + 2])

        # Check space exists on the board
        if (row + 2 <= 7 and column + 1 <= 7):
            # Check space up two and right one - if enemy add to capture list
            if (board.getPiece(row + 2, column + 1) != None and board.getPiece(row + 2, column + 1).getColor() != self.color):
                captureList.append([row + 2, column + 1])

    # Check spaces below the Knight

        # Check space exists on the board
        if (row - 1 >= 0 and column - 2 >= 0):
            # Check space down one anf left two - if enemy add to capture list
            if (board.getPiece(row - 1, column - 2) != None and board.getPiece(row - 1, column - 2).getColor() != self.color):
                captureList.append([row - 1, column - 2])

        # Check space exists on the board
        if (row - 2 >= 0 and column - 1 >= 0):
            # Check space down two and left one - if enemy add to capture list
            if (board.getPiece(row - 2, column - 1) != None and board.getPiece(row - 2, column - 1).getColor() != self.color):
                captureList.append([row - 2, column - 1])

        # Check space exists on the board
        if (row - 1 >= 0 and column + 2 <= 7):
            # Check space down one and right two - if enemy add to capture list
            if (board.getPiece(row - 1, column + 2) != None and board.getPiece(row - 1, column  + 2).getColor() != self.color):
                captureList.append([row - 1, column + 2])
                
        # Check space exists on the board
        if (row - 2 >= 0 and column + 1 <= 7):
            # Check space down two and right one - if enemy add to capture list
            if (board.getPiece(row - 2, column + 1) != None and board.getPiece(row - 2, column + 1).getColor() != self.color):
                captureList.append([row - 2, column + 1])

        return captureList