from abc import ABC, abstractmethod

class Character(ABC):

    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health
    
    @abstractmethod
    def save(self, filename: str) -> None:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass


