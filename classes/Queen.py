from classes.Piece import Piece

class Queen(Piece):
    def create(self, id,  color, position):
        self.id = id
        self.type = "Queen"
        self.color = color
        self.position = position
        self.isCaptured = False
        #print("Creating " + self.color + " " + self.type)

    def giveMoveList(self, position, ):
        print("I move like a Queen")

    def capture(self):
        print("I capture like a Queen")