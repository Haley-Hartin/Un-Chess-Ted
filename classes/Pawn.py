from classes.Piece import Piece

class Pawn(Piece):
    def create(self, id,  color, position):
        self.id = id
        self.type = "Pawn"
        self.color = color
        self.position = position
        self.isCaptured = False
        #print("Creating " + self.color + " " + self.type)

    def giveMoveList(self):
        print("I move like a Pawn")

    def capture(self):
        print("I capture like a Pawn")