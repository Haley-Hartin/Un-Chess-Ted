from __future__ import annotations
from classes.Player import Player
# from classes.ChessGame import ChessGame
from classes.ChessGame import ChessGame
from abc import ABC, abstractmethod

#Pattern - Observer Pattern
class Observer(ABC): # https://refactoring.guru/design-patterns/observer/python/example
    """
    The Observer interface declares the update method, used by Players.
    """

    @abstractmethod
    def update(self, ChessGame: ChessGame) -> None:
        """
        Receive update from Player.
        """
        pass
