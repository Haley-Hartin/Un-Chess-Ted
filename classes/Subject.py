from __future__ import annotations
from abc import ABC, abstractmethod
from classes.Observer import Observer
from typing import List


class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the Subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the Subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass
