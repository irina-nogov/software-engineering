class Mammal:
    className = 'Mammal'

class Dog(Mammal):
    species = 'canine'
    sounds = 'wow'
    def behavior(self):
        return "Dogs are known for their loyalty and obedience"

class Cat(Mammal):
    species = 'feline'
    sounds = 'meow'
    def behavior(self):
        return "Cats are known for their independence and agility"

dog = Dog()
print(f"Dog is {dog.className}, but they say {dog.sounds}. {dog.behavior()}")
cat = Cat()
print(f"Cat is {cat.className}, but they say {cat.sounds}. {cat.behavior()}")