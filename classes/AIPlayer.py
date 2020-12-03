from classes.Player import Player
from classes.Observer import Observer
from typing import List
import numpy as np
import time

class AIPlayer(Player):

   def decideMove(self, moves): #https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html
    return np.random.choice(moves)

   def selectPiece(self, pieces):
       print("Pieces AI can select: " + str(pieces))
       piece_index = np.random.randint(len(pieces)) #https://het.as.utexas.edu/HET/Software/Numpy/reference/generated/numpy.random.randint.html
       return pieces[piece_index]
