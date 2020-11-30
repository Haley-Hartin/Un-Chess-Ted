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
#logging.basicConfig(level=logging.DEBUG)
from classes.ChessGame import ChessGame
import jsonpickle
from json import JSONEncoder

app = Flask(__name__)
app.secret_key = 'some secret key' #can be changes later

@app.route('/', methods=['GET', 'POST'])
def index():
    """navigate to the single player page or multiplayer page"""
    session['image_dict'] = board.board #get the board dictionary from board.py file
    session['num_clicks'] = 0
    session['moves'] = []

    if request.method == 'POST':
        if request.form['submit_button'] == 'Single Player':
                return redirect(url_for('singleplayer_setup')) #if the clicked on singleplayer mode
        elif request.form['submit_button'] == 'MultiPlayer':
                return redirect(url_for('multiplayer_setup')) #if the clicked on multiplayer mode
    return render_template('homepage.html')

@app.route('/multiplayer', methods=['GET', 'POST'])
def multiplayer_setup():
    """get and save the players names for multiplayer mode."""
    error = None

    if request.method == 'POST':
        if 'Back' in request.form: #handle the requests to restart the game
            return redirect(url_for('index')) #call homepage function
        player_one = request.form['firstname']
        player_two = request.form['secondname']
        session['player1'] = player_one #Use sessions to store data between calls
        session['player2'] = player_two
        session['player_turn'] = session['player1']

        game = ChessGame(player_one, player_two, True) #create instance of chess game
        gameJSON = jsonpickle.encode(game, unpicklable=True) #encode it to JSON
        session['game'] = gameJSON #store it in session data
       
        return redirect(url_for('chess')) #call chess()


    return render_template('multiplayer.html', error=error)

@app.route('/singleplayer', methods=['GET', 'POST'])
def singleplayer_setup():
    """get and save the players name and difficulty"""
    error = None
    
    if request.method == 'POST':
        if 'Back' in request.form: #handle the requests to restart the game
            return redirect(url_for('index')) #call homepage function
        player_one = request.form['firstname'] #use request.form[] to get the data from html pages
        difficulty = request.form.get('submit_button')
        session['difficulty'] = difficulty

        session['player1'] = player_one #save player names
        session['player2'] = "Computer"
        session['player_turn'] = session['player1']

        if request.form.get('play') == 'Play': #once the "play" button is pressed, call chess()

            game = ChessGame(player_one, "Computer", False) #create instance of chess game
            empJSON = jsonpickle.encode(game, unpicklable=True) #encode it to JSON
            session['game'] = empJSON #store it in session data
  
            return redirect(url_for('chess'))



    return render_template('singleplayer.html', error=error)



@app.route('/playchess', methods=['GET', 'POST'])
def chess():
    """handle the page where game play occurs
    Future implementation should pass the space selected to the back end to evaluate possible moves.
    Future implememntation should also pass in the space the piece was moved to in order to evaluate a checkmate or tie.
    """

    text = get_text() #get the text to display in html page

    if request.method == 'POST':
        session['moves'] = []
        session['num_clicks'] += 1
        

        if 'Restart' in request.form: #handle the requests to restart the game
            session['image_dict'] = board.board #get the board dictionary from board.py file
            session['player_turn'] = session['player1']
            session['num_clicks']  = 0

        elif 'Quit' in request.form: #handle the requests to restart to quit
            return redirect(url_for('index')) #call homepage function

        elif 'Rules' in request.form:
            return redirect("https://en.wikipedia.org/wiki/Rules_of_chess")

        elif int(session['num_clicks']) == 1: #get the space from first click - the space of the piece to move
            
            session['start space'] = request.form['space'] #get the space selected
            
            pass_move() #pass move to back end
            change_turns()

        elif int(session['num_clicks']) == 2: #get the space from second click - the space to move to

            session['end space'] = request.form['space'] #get the space to move the piece to
            
            check_move() #check the move is valid 
            

    json_converted_moves= json.dumps(session['moves'])
    json_converted_dict = json.dumps(session['image_dict'])
    return render_template('chess.html',
                           display_text = text,
                           image_dict = json_converted_dict,
                           availiable_moves = json_converted_moves)

def get_game_object():
    """Function to decode the chessgame object."""
    return jsonpickle.decode(session['game']) #deocde JSON game object

def store_game_object(gameJSON):
    """function to re encode the chessGame object and store it."""
    gameEncoded = jsonpickle.encode(gameJSON, unpicklable=True)#re encode it to JSON
    session['game'] = gameEncoded #store it back in session data


def change_turns():
    """function to handle switching turns.
    Note: class objects can't be stored within the 'session' dictionary which is why I didn't make a players class.
    """
    if session['player_turn'] == session['player1']:
        session['player_turn'] = session['player2']
    else:
        session['player_turn'] = session['player1']

def pass_move():
    """function to pass the spot to move from to the chessGame class and get a list of legal moves in return."""
    #save the image url from that space
    if session['start space'] in session['image_dict']:
        session['img url'] =  session['image_dict'][session['start space']]

    else:
        session['image_dict'][session['start space']] = ''
        session['img url'] =  ''
    
   
    gameJSON = get_game_object()
    gameJSON.player_wants_move_list(session['start space']) #call class method 
    session['moves'] = ['A1', 'B1', 'C2'] #this is just for testing, should be a function call to get the availiable moves


    store_game_object(gameJSON)


def check_move():
    """Function to check if the spot moved to is valid. Move will get passed to the ChessGame class to be validated."""
    #set the img url on the end space to the img url from the start space
    session['image_dict'][session['end space']] = session['img url']
    session['image_dict'][session['start space']] = "" #remove the img url from the start space
    session['num_clicks']  = 0
    session['moves'] = []
    
    gameJSON = get_game_object()
    gameJSON.player_wants_to_make_move(session['start space'], session['end space'])  #call class method     
    store_game_object(gameJSON)

    
def get_text(): 
    """Get either whose turn it it, or who won the game to display to the front end."""
    gameJSON = get_game_object()
    
    #if game over
    if(gameJSON.game_over() != None):
        text = gameJSON.game_over() + " won!"
        
    #if not game over
    else:
        text = "It is " + session['player_turn'] + "'s turn"
         
    return str(text)



if __name__ == '__main__':
    app.run(debug=True)
