from abc import ABC, abstractmethod

class Character(ABC):

    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health
    
    @abstractmethod
    def save(self, filename: str) -> None:
        """
            each subclass of Character must be saveable.
            they must each implement a save method
        """
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """
            repr defines the string representation of an object
            each subclass of Character should have a unique string representation
        """
        pass


class Fighter(Character):

    def __init__(self, name: str, health: int, speed: int):
        self.speed = speed
        super().__init__(name, health)

    def save(self, filename: str) -> None:
        file = open(filename)
        file.write(f'{self.name},{self.health},{self.speed}')
        file.close()
    
    def __repr__(self) -> str:
        return f'{self.name} the fighter, with {self.health} health and {self.speed} speed'


class Mage(Character):

    def __init__(self, name: str, health: int, mana: int):
        self.mana = mana
        super().__init__(name, health)

    def save(self, filename: str) -> None:
        file = open(filename)
        file.write(f'{self.name},{self.health},{self.mana}')
        file.close()
    
    def __repr__(self) -> str:
        return f'{self.name} the mage, with {self.health} health and {self.mana} mana'


my_fighter = Fighter('eric', 10, 5)
print(my_fighter)