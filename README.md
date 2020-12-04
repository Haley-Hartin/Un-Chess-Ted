# Un-Chess-Ted
## A virtual chess game
### Team Members: Haley Hartin, Blythe Waltman, Haley Drexel.

1. To run the game locally
  * Within the project directory run: ". venv/bin/activate" in your terminal.
  * Then run the site locally with "python3 fileserver.py" within the project directory.
  
 2. Access the game online via heroku here:
   * https://un-chess-ted.herokuapp.com/


3. System Requirments
  * Require that this game will be accessed on a website.
  * Require that this game allows for the user of the website to choose 1 or 2 player mode on the home screen.
  * 1 player mode plays against an AI. 
  * 2 player mode is only played between 2 players using the same computer, the same screen.  Local is defined as 2 players playing from the same computer.
  * Both 1 and 2 player modes have to be able to play a standard game of chess with a GUI 8x8 checkerboard.
  * Each player in each mode will be given a standard set of chess pieces (white and black respectfully): 8 Pawns, 2 Bishops, 2 Rooks, 2 Knights,1 King, 1 Queen.
  * Each piece will appear in the GUI as well.
  * Each player will move one of their pieces on the board using the mouse on their turn. A selected piece (assuming it is the players), will only be able to move on highlighted squares the game says the piece can move to.
  * The players will take turns moving one of their pieces.
  * A player's move may end in the capture of another player's piece. The game will remove the piece from the board if it is captured.
  * The player cannot move into a spot on the board where one of their other pieces are already located.
  * Pieces move according to the rules: https://www.chess.com/terms/chess-pieces.
  * The special rules for pieces will also be implemented.
  * The color of each player will be determined randomly. White will always move first.
  * A game will end when one player puts the other player’s King in checkmate or there are no legal moves left.
  * The game also will identify if a player has put the other player in check.
  * The game will keep track of the moves made in a table.
  * Once the game ends, the player will see a game over screen who won.
  * The player will also have the ability to either return to the home screen or start a new game.



  
