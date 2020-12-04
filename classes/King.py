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

        # Check if there is a row above the king's current location
        if(row + 1 <= 7):
            # Check if there is a column to the left of the king's current location
            if(column - 1 >= 0):
                # If the location up one and to the left one of the king is empty add it to the move list
                if (board.getPiece(row + 1, column - 1) == None):
                    moveList.append([row + 1, column -1])
            # If the location up one of the king is empty add it to the move list
            if (board.getPiece(row + 1, column) == None):
                moveList.append([row + 1, column])
            # Check if there is a column to the right of the king's current location
            if (column + 1 <= 7):
                # If the location up one row and to the right one column is empty add it to the move list
                if (board.getPiece(row + 1, column + 1) == None):
                    moveList.append([row + 1, column + 1])

        # Check if there is a row below the king's current position
        if (row - 1 >= 0):
            # Check if there is a column to the left of the king's current position
            if (column - 1 >= 0):
                # If the location down one and to left one is empty add it to the moves list
                if (board.getPiece(row - 1, column - 1) == None):
                    moveList.append([row - 1, column -1])
            # Check if the location one below the king's current position is empty
            if (board.getPiece(row - 1, column) == None):
                moveList.append([row - 1, column])
            # Check if there is a column to the right of the king's current position
            if (column + 1 <= 7):
                # If the location down one and to the right one of is empty add it to the move list
                if (board.getPiece(row - 1, column + 1) == None):
                    moveList.append([row - 1, column + 1])

        # Check if there is a column to the left of the king
        if(column - 1 >= 0):
            # If the location to the left of the king is empty add it to the moves list
            if (board.getPiece(row, column - 1) == None):
                moveList.append([row, column - 1])
        # Check if there is a column to the right of the king
        if (column + 1 <= 7):
            # If the location to the right of the king is empty add it to the moves list
            if (board.getPiece(row, column + 1) == None):
                moveList.append([row, column + 1])

        return moveList


    def giveCaptureList(self,board):
        captureList = []

        row = self.position[0]
        column = self.position[1]

        # Check if there is a row above the king's current location
        if (row + 1 <= 7):
            # Check if there is a column to the left of the king's current location
            if (column - 1 >= 0):
                # If the location up one and to the left one of the king is an enemy piece add it to the capture list
                if (board.getPiece(row + 1, column - 1) != None and board.getPiece(row + 1, column - 1).getColor() != self.color):
                    captureList.append([row + 1, column - 1])
            # If the location up one of the king is is an enemy piece add it to the capture list
            if (board.getPiece(row + 1, column) != None and board.getPiece(row + 1, column).getColor() != self.color):
                captureList.append([row + 1, column])
            # Check if there is a column to the right of the king's current location
            if (column + 1 <= 7):
                # If the location up one row and to the right one column is an enemy piece add it to the capture list
                if (board.getPiece(row + 1, column + 1) != None and board.getPiece(row + 1, column + 1).getColor() != self.color):
                    captureList.append([row + 1, column + 1])

        # Check if there is a row below the king's current position
        if (row - 1 >= 0):
            # Check if there is a column to the left of the king's current position
            if (column - 1 >= 0):
                # If the location down one and to left one is an enemy piece add it to the capture list
                if (board.getPiece(row - 1, column - 1) != None and board.getPiece(row - 1, column - 1).getColor() != self.color):
                    captureList.append([row - 1, column - 1])
            # Check if the location one below the king's current position is an enemy piece add it to the capture list
            if (board.getPiece(row - 1, column) != None and board.getPiece(row - 1, column).getColor() != self.color):
                captureList.append([row - 1, column])
            # Check if there is a column to the right of the king's current position
            if (column + 1 <= 7):
                # If the location down one and to the right one of is an enemy piece add it to the capture list
                if (board.getPiece(row - 1, column + 1) != None and board.getPiece(row - 1, column + 1).getColor() != self.color):
                    captureList.append([row - 1, column + 1])

        # Check if there is a column to the left of the king
        if (column - 1 >= 0):
            # If the location to the left of the king is an enemy piece add it to the capture list
            if (board.getPiece(row, column - 1) != None and board.getPiece(row, column - 1).getColor() != self.color):
                captureList.append([row, column - 1])
        # Check if there is a column to the right of the king
        if (column + 1 <= 7):
            # If the location to the right of the king is an enemy piece add it to the capture list
            if (board.getPiece(row, column + 1) != None and board.getPiece(row, column + 1).getColor() != self.color):
                captureList.append([row, column + 1])

        return captureList
    
    def is_captured(self):
        return self.isCaptured
    

        