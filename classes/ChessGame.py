from classes.Player import Player
from classes.ChessBoard import ChessBoard

class ChessGame:
    def __init__(self, player_one, player_two, multi_player):
        self.player1_name = player_one
        self.player2_name = player_two
        self.human_vs_human = multi_player
        self.runGame()

    def runHumanVsHuman(self):
        # create white player
        p1 = Player("white", self.player1_name)
        # create black player
        p2 = Player("black", self.player2_name)

    def runGame(self):
        #create board
        board = ChessBoard()

        #create players
        if(self.human_vs_human):
            print("This is a human vs human game")
            print("Player One's name is " + self.player1_name)
            print("Player Two's name is " + self.player2_name)
            self.runHumanVsHuman()
        else:
            print("This is a human vs AI game")
            print("Player One's name is " + self.player1_name)
            print("player Two's name is " + self.player2_name)


game1 = ChessGame("John", "Alice", True)
