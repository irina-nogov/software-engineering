class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"Это {self.name}")

the_animal = Animal("собака")
the_animal.sound()