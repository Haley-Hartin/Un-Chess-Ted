from classes.Subject import Subject
from classes.HumanPlayer import HumanPlayer
from classes.AIPlayer import AIPlayer
# from classes.ChessBoard import ChessBoard
from classes.Observer import Observer
from typing import List
import os
from classes.Player import Player
# from classes.ChessGame import ChessGame

class GameLog(Observer):
    def __init__(self):
        self.turn = []
    
    def create_results_page(self):
        f = open("templates/results.html", "w+")
        content = "<style> table, th, td{ border: 1px solid black;}"
        f.write(content)
        content = "</style> <table style='width:90%'> <tr><th>White Piece</th><th>White Move</th> <th>Black Piece</th><th>Black Move</th></tr>"
        f.write(content)
        f.close()
    
    def reset_page(self):
        curr_dir = os.path.join(os.getcwd(), "templates" )
        if ("results.html" in curr_dir):
            os.remove("templates/results.html")
    
    def write(self):
        print("I am writing to the results page.")
        f = open("templates/results.html", "a")
        f.write("<tr>")
        f.write("<td>"+self.turn[0]+"</td>")
        f.write("<td>"+self.turn[1]+"</td>")
        f.write("<td>"+self.turn[2]+"</td>")
        f.write("<td>"+self.turn[3]+"</td>")
        f.write("</tr>")
        f.close()
        
    def update(self, game):
        print("updating game log: ", game.piece.getID(), " to: ",game.finalLocation)
        self.turn.append(game.piece.getID())
        self.turn.append(str(game.finalLocation))
        self.reset_turns()
    
    def reset_turns(self): 
        print("length of turns array: " , len(self.turn))
        print(self.turn)
        if(len(self.turn)==4):
            print("Both players have made a move.")
            self.write()
            self.turn = []
        
