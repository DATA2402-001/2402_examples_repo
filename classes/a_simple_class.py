
class Character:  # convention is camel case for class names
    
    def __init__(self, character_name: str, character_hp: int) -> None:
        self.name = character_name
        self.hit_points = character_hp


my_character = Character('eric', 5)
my_other_character = Character('Daniel', 1)
print(f'{my_character.name} has {my_character.hit_points} hp')
print(f'{my_other_character.name} has {my_other_character.hit_points} hp')

