class Human:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Привет, {self.name}!")

    @classmethod
    def species(cls):
        return "Homosapiens"

    @staticmethod
    def message():
        return "Это произвольное сообщение."

hm = Human("Maksim")
hm.greet()
print(Human.species())
print(Human.message())
