from abc import ABCMeta, abstractmethod

class Piece(metaclass=ABCMeta):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def giveMoveList(self, board):
        pass

    @abstractmethod
    def giveCaptureList(self, board):
        pass

    def convertList(self, finalList):
        stringList = []
        file = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for pair in finalList:
            position = file[pair[1]] + str(pair[0] + 1 )
            stringList.append(position)
        return stringList

    def combineList(self, moves, captures):
        if (moves != None and captures != None):
            finalList = moves + captures
        elif (moves != None and captures == None):
            finalList = moves
        elif (moves == None and captures != None):
            finalList = captures
        else:
            return None
        return finalList

    #Pattern - Template method: Defines the skeleton for the operation to get a complete list of moves (both normal moves and captures)
    def getList(self, board):
        moveList = self.giveMoveList(board) # Get normal moves - hook method
        captureList = self.giveCaptureList(board) # Get capture moves - hook method
        finalList = self.combineList(moveList, captureList) # Compute whether to add the lists - helper method
        if(finalList == None):
            return None
        convertedList = self.convertList(finalList) # Convert the array list back to rank and file for json format - helper method
        return convertedList

    def getId(self):
        return self.id

    def setId(self, pawn_id):
        self.id = id

    def getColor(self):
        return self.color

    def setColor(self, player_color):
        self.color = player_color

    def getPosition(self):
        return self.position

    def setPosition(self, pawn_position):
        self.position = pawn_position

    def getIsCaptured(self):
        return self.isCaptured

    def setIsCaptured(self, capture_bool):
        self.isCaptured = capture_bool

    def getPieceType(self):
        return self.type
