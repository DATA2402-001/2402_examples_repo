from abc import ABC, abstractmethod

class Character(ABC):

    @abstractmethod
    def save(self,filename: str) -> None:
        pass


class Mage(Character):
    
    def save(self, filename):
        # 


my_mage = Mage()