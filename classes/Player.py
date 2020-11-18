from __future__ import annotations
from abc import ABC, abstractmethod


class Player():
    def __init__(self, player_color, player_name):
        self.color = player_color
        self.name = player_name
