from classes.Subject import Subject
from classes.HumanPlayer import HumanPlayer
from classes.AIPlayer import AIPlayer
from classes.ChessBoard import ChessBoard
from classes.Observer import Observer
from typing import List
import os
from classes.Player import Player

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
        os.remove("../templates/results.html")
    
    def write(self):
        f = open("templates/results.html", "a")
        f.write("<tr>")
        f.write("<td>"+self.turn[0]+"</td>")
        f.write("<td>"+self.turn[1]+"</td>")
        f.write("<td>"+self.turn[2]+"</td>")
        f.write("<td>"+self.turn[3]+"</td>")
        f.write("</tr>")
        f.close()
        
    def update(self, player: Player):
        print()
        print("Board: I was just notified that the player would like to move the piece that is at location " +   str(player.piece.getID()) + str(player.finalLocation) )
        self.reset_turns()
        self.turn.append(player.piece.getID())
        self.turn.append(str(player.finalLocation))
        print(self.turn)
    
    def reset_turns(self): 
        
        if(len(self.turn)==4):
            self.write()
            self.turn = []
        
