from classes.Subject import Subject
from classes.HumanPlayer import HumanPlayer
from classes.AIPlayer import AIPlayer
from classes.ChessBoard import ChessBoard
from classes.Observer import Observer
from typing import List

class ChessGame(Subject):
    def __init__(self, player_one, player_two, multi_player):
        self.gameOver = False
        self.whitesTurn = True
        self.player1_name = player_one
        self.player2_name = player_two
        self.human_vs_human = multi_player
        self.whitePlayer = None
        self.blackPlayer = None
        self.gameBoard = None
        self.runGame()

    """
        The Subject owns some important state and notifies observers when the state
        changes.
    """

    locationSelected: int = None # Right this is just an int but it should be in the form [x,y] that correspond to board array
    finalLocation: int = None # Right this is just an int but it should be in the form [x,y] that correspond to board array

    """
    For the sake of simplicity, the Player's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("ChessGame: Attached an observer.")
        print()
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Player: Notifying observers...")
        for observer in self._observers:
            observer.update(self)


    def createHumanPlayers(self):
        # create white player
        self.whitePlayer = HumanPlayer("white", self.player1_name)
        # create black player
        self.blackPlayer = HumanPlayer("black", self.player2_name)

    def createHumanAndAIPlayer(self):
        # create white player
        self.whitePlayer = HumanPlayer("white", self.player1_name)
        # create black player
        self.blackPlayer = AIPlayer("black", self.player2_name)

    def runGame(self):
        # create board
        self.gameBoard = ChessBoard()
        self.attach(self.gameBoard)

        # create players
        if(self.human_vs_human):
            print("This is a human vs human game")
            print("Player One's name is " + self.player1_name)
            print("Player Two's name is " + self.player2_name)
            self.createHumanPlayers()
            print()
        else:
            print("This is a human vs AI game")
            print("Player One's name is " + self.player1_name)
            print("player Two's name is " + self.player2_name)
            print()


    def player_wants_move_list(self, location):
        print("A player wants the moves")
        # check if the game is still running
        if(self.gameOver != True):
            print("The game isn't over I will get the move list")
            print("The player wants the moves for the piece at location " + str(location))
            # check whose turn it is
            # check that the piece that is selected is the color of whose turn it is
            # Have player object request move list
        else:
            print("The game is over I can't return a move list")

    def player_wants_to_make_move(self, initalLocation, finalLocation):
        
        self.locationSelected = initalLocation
        self.finalLocation = finalLocation
        print("A player wants to make a move")
        # check if the game is still running
        if(self.gameOver != True):
            print("The game is not over I will update the board")

            # get the color of the piece selected
            color = self.gameBoard.getPieceColor(initalLocation)

            # check that the color to move is the current players color
            if(color == "white" and self.whitesTurn == True):
                # It's white's turn and they want to move a white piece
                self.notify() # Observer method - notify the chess board that the player is moving a piece

                # Check if the game is over now

                # If the game isn't over change the turn to be black's
                self.whitesTurn = False

            elif(color == "black" and self.whitesTurn == False):
                # It's black's turn and they want to move a black piece
                self.notify() # Observer method - notify the chess board that the player is moving a piece

                # If the game isn't over change the turn to be white's
                self.whitesTurn = True

        else:
            print("The game is over I can't move any pieces")
    
    def game_over(self):
        # if the game if over, return the winner, if not, return nothing
        if(self.gameOver):
            print("here")
            return self.player1_name #just for testing, will need to determine winner
        else:
            return None
            
        


#game1 = ChessGame("John", "Alice", True)
#game1.player_wants_to_make_move(2,3)