
class AssignmentDict(dict):

    # no need for an __init__ method here
    # since our class doesn't have unique attributes
    # def __init__(self):
    #     super().__init__()

    def avg_score(self) -> float:
        avg = sum(self.values()) / len(self)  # finding the avg of "my own" (self) values
        return avg
    
    def best_assignment(self) -> str:
        best_key = ''
        max_value = 0
        for key, value in self.items():  # looping through "my own" keys and values
            if value > max_value:
                max_value = value
                best_key = key
        return best_key


scores = AssignmentDict()
scores['assign1'] = 75
scores['assign2'] = 95
scores['assign3'] = 80
print(scores.avg_score())
print(scores.best_assignment())