# Un-Chess-Ted
a virtual chess game

Within the project directory run "python3 -m venv venv"
Before you start work, activate the venv environment: ". venv/bin/activate"
Make sure you install Flask "pip install Flask"
Install flask-session to allow data to be stored between calls "pip install Flask-Session"
This site provides more detial on installing Flask https://flask.palletsprojects.com/en/1.1.x/installation/

To run the site locally run "python3 fileserver.py"

The fileserver.py file handles all the requests between the html pages and back-end.
To store any data in fileserver.py use session['variable'] = value_to_store. It won't save data between calls any other way.
To access data from html pages, use variable = request.form['name of html component']
ex. 
 in html file :
  <input type="text" name="firstname" placeholder="username">
 in fileserver.py file:
  playerone_username = request.form['firstname']
 
 To dynamically change text on the html pages:
 ex.
  in html file :
    <h1> It is {{ player }}'s turn</h1>
  in fileserver.py file:
    return render_template('html_file.html', player = str(session['player_one']))
  
