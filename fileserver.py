"""File to handle requests between front end and back end"""
from flask import Flask
from flask import Flask, render_template, redirect, url_for, request
from flask import session
from os import environ

app = Flask(__name__)
app.secret_key = 'some secret key' #can be changes later


@app.route('/', methods=['GET', 'POST'])
def index():
    """navigate to the single player page or multiplayer page"""
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
        player_one = request.form['firstname']
        player_two = request.form['secondname']
        session['player1'] = player_one #Use sessions to store data between calls 
        session['player2'] = player_two
        return redirect(url_for('chess')) #call chess()


    return render_template('multiplayer.html', error=error)

@app.route('/singleplayer', methods=['GET', 'POST'])
def singleplayer_setup():
    """get and save the players name and difficulty"""
    error = None
    if request.method == 'POST':
        player_one = request.form['firstname'] #use request.form[] to get the data from html pages
        difficulty = request.form.get('submit_button')
        session['difficulty'] = difficulty
        session['player1'] = player_one
        if request.form.get('play') == 'Play': #once the "play" button is pressed, call chess()
            return redirect(url_for('chess'))
        session['num_clicks'] = 0
        session['end space'] = 'nan'
        session['start space'] = 'nan'
        
    return render_template('singleplayer.html', error=error)

      
       
@app.route('/playchess', methods=['GET', 'POST'])
def chess():
    """handle the page where game play occurs
    Future implementation should get the space each player is on and pass it to the backend.
    """
    

    if request.method == 'POST':
        
        if int(session['num_clicks']) > 2: #reset the start and end space for the next turn
            session['num_clicks'] = 0
            session['end space'] = 'nan'
            session['start space'] = 'nan'

        if int(session['num_clicks']) == 0: #get the space from first click - the space of the piece to move
            session['start space'] = request.form['space']
        elif int(session['num_clicks']) == 1: #get the space from second click - the space to move to
            session['end space'] = request.form['space']
        session['num_clicks'] += 1
    #only the first two chess spaces work for now
    #the img passed in will have to be changed each time, the img now is just for testing 
    return render_template('chess.html', player = str(session['player1']), img = "https://i.ibb.co/fYDhhJf/chesspawn.png", new_space = session['end space'], old_space = session['start space']  )




if __name__ == '__main__':
    app.run(debug=True)