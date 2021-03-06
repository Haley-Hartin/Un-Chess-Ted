"""File to handle requests between front end and back end"""
from flask import Flask
from flask import Flask, render_template, redirect, url_for, request
from flask import session
from os import environ
import json
import board
import sys
import logging
import json
from classes.ChessGame import ChessGame
import jsonpickle
from json import JSONEncoder

app = Flask(__name__)
app.secret_key = 'some secret key'
TEMPLATES_AUTO_RELOAD=True
app.jinja_env.auto_reload = True
app.config["TEMPLATES_AUTO_RELOAD"] = True


"""
https://pypi.org/project/jsonpickle/0.3.0/
refrence for encoding/decoding JSON objects

https://www.tutorialspoint.com/flask/flask_routing.htm
Refrence for Flask routing
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    """navigate to the single player page or multiplayer page"""
    session['image_dict'] = board.board #get the board dictionary from board.py file
    session['num_clicks'] = 0
    session['moves'] = []
    session["valid_selection"] = False
    session['html'] = ''

    """
    https://pythonbasics.org/flask-sessions/
    Refrence for using session data

    https://www.w3schools.com/html/html_scripts.asp
    Refrences for html, javascript and css
    """

    if request.method == 'POST':
        if request.form['submit_button'] == 'Single Player':
                return redirect(url_for('singleplayer_setup')) #if the clicked on singleplayer mode
        elif request.form['submit_button'] == 'Multiplayer':
                return redirect(url_for('multiplayer_setup')) #if the clicked on multiplayer mode

    return render_template('homepage.html')

@app.route('/multiplayer', methods=['GET', 'POST'])
def multiplayer_setup():
    """get and save the players names for multiplayer mode."""
    error = None
    print(request.form)
    if request.method == 'POST':
        if 'Back' in request.form: #handle the requests to restart the game
            return redirect(url_for('index')) #call homepage function

        player_one = request.form['firstname']
        player_two = request.form['secondname']
        session['player_one'] = request.form['firstname']
        session['player_two'] = request.form['secondname']
        session['player_turn'] = player_one
        session["game_mode"] = "Multiplayer"
        session['html'] = 'multi_chess.html'

        game = ChessGame(player_one, player_two, True) #create instance of chess game
        game.createHumanPlayers()
        store_game_object(game)

        if 'Back' in request.form: #handle the requests to restart the game
            return redirect(url_for('index')) #call homepage function

        if 'Play' in request.form: #once the "play" button is pressed, call chess()
            return redirect(url_for('chess'))
    return render_template('multiplayer.html', error=error)

@app.route('/singleplayer', methods=['GET', 'POST'])
def singleplayer_setup():
    """get and save the players name and difficulty"""
    error = None

    if request.method == 'POST':
        player_one = request.form['firstname'] #use request.form[] to get the data from html pages
        session['player_turn'] = player_one
        session['player_one'] = player_one
        session['player_two'] = "Computer"
        session["game_mode"] = "Single Player"
        session['html'] = 'single_chess.html'

        game = ChessGame(player_one, "Computer", False) #create instance of chess game
        game.createHumanAndAIPlayer()
        store_game_object(game)

        if 'Back' in request.form: #handle the requests to restart the game
            return redirect(url_for('index')) #call homepage function

        if request.form.get('play') == 'Play': #once the "play" button is pressed, call chess()
            return redirect(url_for('chess'))



    return render_template('singleplayer.html', error=error)



@app.route('/playchess', methods=['GET', 'POST'])
def chess():
    """handle the page where game play occurs
    Future implementation should pass the space selected to the back end to evaluate possible moves.
    Future implememntation should also pass in the space the piece was moved to in order to evaluate a checkmate or tie.
    """
    session['moves'] = []
    text = get_player() #get the text to display in html page
    print(text)
    session['highlighted'] = []

    gameJSON = get_game_object()
    turn = gameJSON.get_player_turn_name()
    print("Player's turn: "  +  turn)

    updatePromotedPawn() #make sure all promoted pawns have been updated to proper image

    if request.method == 'POST':
        session['moves'] = []
        print(request.form)
        if ("Get_Computer_Move" in request.form and turn == "Computer"): #handles request to get the computer's turn
            print("in AI if")
            ai_player_takes_turn()
            app.jinja_env.cache = {}
        elif ("Get_Computer_Move" in request.form and turn != "Computer"):
            pass

        elif 'Restart' in request.form: #handle the requests to restart the game
            session['image_dict'] = board.board #get the board dictionary from board.py file
            session['player_turn'] = session['player_one']
            gameJSON = get_game_object()
            gameJSON.reset_results()
            gameJSON.runGame()
            store_game_object(gameJSON)

            session["valid_selection"] = False

        elif 'Quit' in request.form: #handle the requests to quit
            gameJSON = get_game_object()
            gameJSON.reset_results()
            return redirect(url_for('index')) #call homepage function #https://flask.palletsprojects.com/en/1.1.x/quickstart/

            store_game_object(gameJSON)

        elif 'Rules' in request.form: #handle request to go to the rules
            return redirect("https://en.wikipedia.org/wiki/Rules_of_chess")

        elif 'View Moves' in request.form: #handle the requests to see results of the game
            return render_template('results.html')

        elif (session["valid_selection"] == False and turn != "Computer"): #get the space from first click - the space of the piece to move

            session['start space'] = request.form['space'] #get the space selected
            session['highlighted'] = [session['start space']]

            pass_move() #pass move to back end

        elif  (session["valid_selection"] == True and turn != "Computer"): #get the space from second click - the space to move to

            session['end space'] = request.form['space'] #get the space to move the piece to
            session['highlighted'] = []

            check_move() #check the move is valid
    text = get_text()

    json_converted_moves= json.dumps(session['moves'])
    json_converted_dict = json.dumps(session['image_dict'])
    json_highlighted = json.dumps(session['highlighted'])
    print(text)

    return render_template(session['html'],
                           display_text = text,
                           image_dict = json_converted_dict,
                           availiable_moves = json_converted_moves,
                           highlight =  json_highlighted
                          )

def get_game_object():
    """Function to decode the chessgame object."""
    return jsonpickle.decode(session['game']) #deocde JSON game object

def store_game_object(gameJSON):
    """function to re encode the chessGame object and store it."""
    gameEncoded = jsonpickle.encode(gameJSON, unpicklable=True)#re encode it to JSON
    session['game'] = gameEncoded #store it back in session data


def pass_move():
    """function to pass the spot to move from to the chessGame class and get a list of legal moves in return."""
    #save the image url from that space
    if session['start space'] in session['image_dict']:
        session['img url'] =  session['image_dict'][session['start space']]

    else:
        session['image_dict'][session['start space']] = ''
        session['img url'] =  ''


    gameJSON = get_game_object()
    session['moves'] = gameJSON.player_wants_move_list(session['start space']) #get the available moves at the given initial location
    gameJSON.gameBoard.print_board()
    session['player_turn'] = gameJSON.get_player_turn_name()
    print("The turn should change to ", session['player_turn'])

    #verify the selection the player made
    if(gameJSON.valid_selection(session['start space']) and len(session["moves"]) > 0):
        session["valid_selection"] = True
    else:
        session["valid_selection"] = False

    store_game_object(gameJSON)


def check_move():
    """Function to check if the spot moved to is valid. Move will get passed to the ChessGame class to be validated."""
    gameJSON = get_game_object()
    allowed = gameJSON.player_wants_to_make_move(session['start space'], session['end space'])  # call class method
    gameJSON.gameBoard.print_board()
    store_game_object(gameJSON)
    if(allowed == True):
        #set the img url on the end space to the img url from the start space
        session['image_dict'][session['end space']] = session['img url']
        session['image_dict'][session['start space']] = "" #remove the img url from the start space
        session["valid_selection"] = False
        session['moves'] = []
        #update the player turn
        gameJSON = get_game_object()
        session['player_turn'] = gameJSON.get_player_turn_name()
        store_game_object(gameJSON)

    elif(allowed == False):
        session["valid_selection"] = False
        session['moves'] = []
        #update the player turn
        gameJSON = get_game_object()
        session['player_turn'] = gameJSON.get_player_turn_name()
        store_game_object(gameJSON)


def get_text():
    """Get either whose turn it it, or who won the game to display to the front end."""
    gameJSON = get_game_object()
    game_state = gameJSON.check_game_over()

    if game_state == 'over':
        text = gameJSON.get_player_turn_name() + "'s king is captured!"
    elif game_state == 'Stalemate':
        text = "There are no moves left. The game ends in a Stalemate."
    elif game_state == 'check':
        text = gameJSON.get_player_turn_name() + "'s king is in check. " + gameJSON.get_player_turn_name() + "'s turn "
    elif game_state != None:
        text = gameJSON.get_player_turn_name() + "'s king is in check, and has nowhere to move. " + game_state + " won!"
    else:
         text = "It is " + gameJSON.get_player_turn_name() + "'s turn - " + gameJSON.get_player_turn_color()

    store_game_object(gameJSON)
    return str(text)


def get_player():
    gameJSON = get_game_object()
    game_state = gameJSON.check_game_over()
    text = "It is " + gameJSON.get_player_turn_name() + "'s turn - " + gameJSON.get_player_turn_color()
    store_game_object(gameJSON)
    return text

# run a single turn of the AI
def ai_player_takes_turn():
    gameJSON = get_game_object()
    ai_move_made  = gameJSON.ai_player_turn() #get the initial location and final location the AI made
    store_game_object(gameJSON)

    print("move the ai made:" + str(ai_move_made))
    if(ai_move_made != None): #move the piece from the initial location to the final location
        session['image_dict'][ai_move_made[1]] = session['image_dict'][ai_move_made[0]]
        session['image_dict'][ai_move_made[0]] = ""


#get the locations where a promoted pawn (queen) exists and update their images
def updatePromotedPawn():
    gameJSON = get_game_object()
    promotions = gameJSON.checkPawnpromotion() #get the locations of promoted pawns
    store_game_object(gameJSON)
    for p in promotions: # update the images with queen and the corresponding color
        if(session['image_dict'][p] == board.white_pawn):
            session['image_dict'][p] = board.white_queen
        elif(session['image_dict'][p] == board.black_pawn):
            session['image_dict'][p] = board.black_queen

@app.before_request
def before_request():
    app.jinja_env.cache = {}

if __name__ == '__main__':
    app.before_request(before_request)
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')
