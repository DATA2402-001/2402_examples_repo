from random import random

class Coin:

    def __init__(self, heads_probability):
        "init initializes data attributes"
        self.sideup = 'heads'
        self.heads_probability = heads_probability

    def toss(self) -> None:
        "toss coin (randomly select heads/tails)"
        if random() < self.heads_probability:
            self.sideup = 'heads'
        else:
            self.sideup = 'tails'


my_coin = Coin(0.9)
my_other_coin = Coin(0.1)

for _ in range(10):
    my_coin.toss()
    my_other_coin.toss()
    print(my_coin.sideup, my_other_coin.sideup)