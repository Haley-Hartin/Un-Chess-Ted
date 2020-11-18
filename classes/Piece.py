from abc import ABCMeta, abstractmethod

class Piece(metaclass=ABCMeta):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def giveMoveList(self, position, ):
        pass

    @abstractmethod
    def capture(self):
        pass

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

