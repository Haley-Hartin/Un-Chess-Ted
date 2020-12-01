from classes.Subject import Subject
from classes.HumanPlayer import HumanPlayer
from classes.AIPlayer import AIPlayer
from classes.ChessBoard import ChessBoard
from classes.GameLog import GameLog
from classes.Observer import Observer
from typing import List


class ChessGame(Subject):
    def __init__(self, player_one, player_two, multi_player):
        self.gameOver = False
        self.whitesTurn = True
        self.player1_name = player_one
        self.player2_name = player_two
        self.currentMoveList = []
        self.human_vs_human = multi_player
        self.whitePlayer = None
        self.blackPlayer = None
        self.gameBoard = None
        self.runGame()

    """
        The Subject owns some important state and notifies observers when the state
        changes.
    """

#     locationSelected: int = None # Right this is just an int but it should be in the form [x,y] that correspond to board array
#     finalLocation: int = None # Right this is just an int but it should be in the form [x,y] that correspond to board array
#     piece = None
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
        self.gameLog = GameLog()
        self.gameLog.create_results_page()
        self.attach(self.gameLog)
        self.gameBoard = ChessBoard()
      

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

    # This function takes the location of the piece from the board for example H2 and converts it to the corresponding location in the array
    def convert_piece_location(self, location):

        file = ['A','B','C','D','E','F','G','H']
        if(location != None):
            for i in range (8):
                if(location[0] == file[i]):
                    column = i
        row = int(location[1]) - 1
        print("The piece is at location: [" + str(row) + ", " + str(column) + "] in the board array")
        array_positon = [row, column]
        return array_positon

    def player_wants_move_list(self, location):
        # check if the game is still running
        if(self.gameOver != True):
            print("The game isn't over I will get the move list")
            print("The player wants the moves for the piece at location " + str(location))
            array_location = self.convert_piece_location(str(location))
            pieceColor = self.gameBoard.getPieceColor(array_location[0], array_location[1])

            
            if(pieceColor == None):
                print("No piece at that location")
                return None

            if(self.whitesTurn == True and pieceColor == "white"):
                print("It's white's turn and they want to move a white piece -- I will get move list")
                possibleMoves = self.gameBoard.getMoveListForPiece(array_location[0], array_location[1], pieceColor)
                if(possibleMoves is not None):
                    self.currentMoveList = possibleMoves
                    return possibleMoves

            elif(self.whitesTurn == False and pieceColor == "black"):
                print("It's black's turn and they want to move a black piece -- I will get move list")
                possibleMoves = self.gameBoard.getMoveListForPiece(array_location[0], array_location[1], pieceColor)
                if (possibleMoves is not None):
                    self.currentMoveList = possibleMoves
                    return possibleMoves
            else:
                print("The piece color does not match whose player's turn it is -- I will not give a move list")


            # check whose turn it is
            # check that the piece that is selected is the color of whose turn it is
            # Have player object request move list
        else:
            print("The game is over I can't return a move list")

    def player_wants_to_make_move(self, initalLocation, finalLocation):
        array_location = self.convert_piece_location(str(initalLocation))
        
        self.locationSelected = initalLocation
        self.finalLocation = finalLocation
        self.piece = self.gameBoard.getPiece(array_location[0], array_location[1])

        print("Player wants to move piece from " + initalLocation + " to " + finalLocation)

        # check if the game is still running
        if(self.gameOver != True):

            # get the color of the piece selected

            array_intial_location = self.convert_piece_location(str(initalLocation))
            array_final_location = self.convert_piece_location(str(finalLocation))

            color = self.gameBoard.getPieceColor(array_intial_location[0], array_intial_location[1])

            # check that the color to move is the current players color
            if(color == "white" and self.whitesTurn == True):
                # It's white's turn and they want to move a white piece
                print(self.piece.getID())
                print(self.finalLocation )
                self.notify() # Observer method - notify the chess board that the player is moving a piece

                if(finalLocation in self.currentMoveList):
                    print("that move is allowed")
                    self.whitesTurn = False
                    self.gameBoard.updateBoard(array_intial_location[0], array_intial_location[1], array_final_location[0], array_final_location[1])
                    return True
                else:
                    print("that move is not allowed")
                    return False


            elif(color == "black" and self.whitesTurn == False):
                self.notify() # Observer method - notify the chess board that the player is moving a piece
                if (finalLocation in self.currentMoveList):
                    print("that move is allowed")
                    self.whitesTurn = True
                    self.gameBoard.updateBoard(array_intial_location[0], array_intial_location[1],array_final_location[0], array_final_location[1])
                    return True
                else:
                    print("that move is not allowed")
                    return False

        else:
            print("The game is over I can't move any pieces")

        

    def check_game_over(self):
        if self.whitesTurn:
            color = 'white'
            winner = self.blackPlayer
        else:
            color = 'black'
            winner = self.whitePlayer
        print("Checking if " + color + " has any moves to make.")
       
        # if the game if over, return the winner, if not, return nothing
        if self.gameBoard.check_stalemate(color):
            self.gameOver = True
            self.gameLog.reset_page()
            return "Stalemate"  # just for testing, will need to determine winner
        elif self.gameBoard.check_checkmate(color):
            return winner
            self.gameOver = True
        else:
            return None
    
    def get_player_turn_name(self):

        if self.whitesTurn:
            return self.whitePlayer.get_name()
        else:
            return self.blackPlayer.get_name()
    
    def get_player_turn_color(self):
        if self.whitesTurn:
            return "white"
        else:
            return "black"

        

#game1 = ChessGame("John", "Alice", True)
#game1.player_wants_to_make_move(2,3)
