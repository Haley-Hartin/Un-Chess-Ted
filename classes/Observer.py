from __future__ import annotations
from classes.Player import Player
from abc import ABC, abstractmethod

class Observer(ABC):
    """
    The Observer interface declares the update method, used by Players.
    """

    @abstractmethod
    def update(self, Player: Player) -> None:
        """
        Receive update from Player.
        """
        pass
