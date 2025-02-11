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


my_fighter = Fighter('eric', health=10, speed=5)
my_mage = Mage('harry potter', health=5, mana=20)


def mana_boost(mage: Mage, amount: int) -> None:
    
    if type(mage) == Mage:
        mage.mana += amount
    else:
        raise TypeError('mage must be a Mage object')


def health_boost(character: Character, amount: int) -> None:
    if isinstance(character, Character):
        character.health += amount
    else:
        raise TypeError('character must be a Character subclass')

print(my_mage.mana)
mana_boost(my_mage, 5)
print(my_mage.mana)

print(my_fighter.health)
health_boost("abcde", 10)
print(my_fighter.health)