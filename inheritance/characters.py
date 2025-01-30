class Character:

    def __init__(self, name: str, strength: int, dexterity: int):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
    
    def save(self, filename: str) -> None:
        file = open(filename, 'w')
        file.write(self.name + ',')
        file.write(str(self.strength) + ',')
        file.write(str(self.dexterity))
        file.close()


class Mage(Character):

    def __init__(self, name: str, strength: int, dexterity: int, mana: int):
        self.mana = mana
        self.spells = []
        super().__init__(name, strength, dexterity)
    
    def add_spell(self, spell_name: str)-> None:
        self.spells.append(spell_name)


class Wizard(Mage):

    def __init__(self, name: str, strength: int, dexterity: int, mana: int, school: str):
        self.school_of_magic = school
        super().__init__(name, strength, dexterity, mana)
    

the_wizard = Wizard("wizard of oz", 5, 10, 1, "illusion")
the_wizard.save('temp.txt')