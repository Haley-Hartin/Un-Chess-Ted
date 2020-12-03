from __future__ import annotations
from abc import ABC, abstractmethod


class Player(ABC): #https://docs.python.org/3/library/abc.html
    def __init__(self, player_color, player_name):
        self.color = player_color
        self.name = player_name
    def get_name(self):
        return self.name
    def get_color(self):
        return self.color

    @abstractmethod
    def decideMove(self, moves):
        pass
