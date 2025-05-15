class Animal:
    def __init__(self, name, species,legs):
        self.name = name
        self.species = species
        self.legs = legs

    def make_sound(self):
            return "Some generic sound"
class Mammal(Animal):
    def make_sound(self):
        return "Roar"

    def give_birth(self):
        return f"{self.name} gives birth to live young."

class Bird(Animal):
    def make_sound(self):
        return "Squawk"
    def lay_eggs(self):
        return f"{self.name} lays eggs."
class Reptile(Animal):
    def make_sound(self):
        return "Hiss"

    def shed_skin(self):
        return f"{self.name} sheds its skin."