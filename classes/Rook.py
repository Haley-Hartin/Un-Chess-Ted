from classes.Piece import Piece

class Rook(Piece):
    def create(self, id, color, position):
        self.id = id
        self.type = "Rook"
        self.color = color
        self.position = position
        self.isCaptured = False
        #print("Creating " + self.color + " " + self.type)

    def move(Piece):
        print("I move like a Rook")

    def capture(Piece):
        print("I capture like a Rook")