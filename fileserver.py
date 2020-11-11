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
        if difficulty != None:
            return redirect(url_for('submit'))
        
    return render_template('singleplayer.html', error=error)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    """handle submit button for singleplayer page."""
    if request.method == 'POST':
        if request.form.get('play') == 'Play':
                return redirect(url_for('chess'))
    return render_template('singleplayer.html')
   

        
       
@app.route('/playchess', methods=['GET', 'POST'])
def chess():
    """handle the page where game play occurs
    Future implementation should get the space each player is on and pass it to the backend.
    """
    return render_template('chess.html', player = str(session['player1']))




if __name__ == '__main__':
    app.run(debug=True)