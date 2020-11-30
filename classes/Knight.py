from classes.Piece import Piece

class Knight(Piece):
    def create(self, id,  color, position):
        self.id = id
        self.type = "Knight"
        self.color = color
        self.position = position
        self.isCaptured = False
        #print("Creating " + self.color + " " + self.type)

    def giveMoveList(self, position, ):
        print("I move like a Knight")

    def giveCaptureList(self,board):
        print("I capture like a Knight")