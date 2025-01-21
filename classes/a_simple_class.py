
class Character:  # convention is camel case for class names
    
    def __init__(self, character_name: str, character_hp: int, damage: int) -> None:
        self.name = character_name
        self.hit_points = character_hp
        self.damage = damage

my_character = Character('eric', 5, 1)
my_other_character = Character('Daniel', 1, 1_000_000)
print(f'{my_character.name} has {my_character.hit_points} hp')
print(f'{my_other_character.name} has {my_other_character.hit_points} hp')

def attack(attacker: Character, defender: Character) -> None:
    # hp_remaining = defender.hit_points - attacker.damage
    # defender.hit_points = hp_remaining

    # more concise
    defender.hit_points -= attacker.damage

attack(my_other_character, my_character)
print(my_character.hit_points)

