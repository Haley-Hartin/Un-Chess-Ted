from classes.Piece import Piece

class King(Piece):
    def create(self, id,  color, position):
        self.id = id
        self.type = "King"
        self.color = color
        self.position = position
        self.isCaptured = False
        #print("Creating " + self.color + " " + self.type)

    def giveMoveList(self, position, ):
        print("I move like a King")

    def giveCaptureList(self,board):
        print("I capture like a King")
    
    def is_captured(self):
        return self.isCaptured