class Vertebrate:

    def __init__(self, n_vertebrae: int):
        self.num_vertebrae = n_vertebrae
    

class Frog(Vertebrate):
    
    def __init__(self, is_poisonous: bool):
        self.is_poisonous = is_poisonous
        super().__init__(10) # frogs have 10, so hard code that


kermit = Frog(False)
print(kermit.is_poisonous)
print(kermit.num_vertebrae)
