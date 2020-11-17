from classes.Piece import Piece

class Bishop(Piece):
    def create(self, id,  color, position):
        self.id = id
        self.type = "Bishop"
        self.color = color
        self.position = position
        self.isCaptured = False
        #print("Creating " + self.color + " " + self.type)

    def move(self):
        print("I move like a Bishop")

    def capture(self):
        print("I capture like a Bishop")