class Vertebrate:

    def __init__(self, n_vertebrae: int):
        self.num_vertebrae = n_vertebrae
    

class Frog(Vertebrate):
    
    def __init__(self, is_poisonous: bool):
        self.is_poisonous = is_poisonous
        super().__init__(10) # frogs have 10, so hard code that

class Dog(Vertebrate):

    def __init__(self, sheds_on_carpet: bool, name: str, num_of_vertebrae: int):
        self.sheds_on_carpet = sheds_on_carpet
        self.name = name
        super().__init__(num_of_vertebrae)



kermit = Frog(False)
print(kermit.is_poisonous)
print(kermit.num_vertebrae)

bryans_dog = Dog(False, "Happy", 51)
print(bryans_dog.name)
print(bryans_dog.num_vertebrae) # dog inherits this from Vertebrate
print(bryans_dog.poisonous) # this won't work: poisonous is a Frog attribute

some_animal = Vertebrate(1000)
