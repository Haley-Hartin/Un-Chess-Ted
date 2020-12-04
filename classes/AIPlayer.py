from classes.Player import Player
from classes.Observer import Observer
from typing import List
import numpy as np
import time

#The class for the AI player when a player chooses single player mode
#The AI's logic is very simple: it chooses a random piece and once it chooses a random piece, it will choose a random move
class AIPlayer(Player):

    #choose a random move from a given list
   def decideMove(self, moves): #https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html
    return np.random.choice(moves)

    #choose a random piece from the list given
   def selectPiece(self, pieces):
       #print("Pieces AI can select: " + str(pieces))
       piece_index = np.random.randint(len(pieces)) #https://het.as.utexas.edu/HET/Software/Numpy/reference/generated/numpy.random.randint.html
       return pieces[piece_index]
