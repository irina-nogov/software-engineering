class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Гав!"


class Cat(Animal):
    def sound(self):
        return "Мяу!"


dog = Dog("Собака")
cat = Cat("Кот")

print(f"{dog.name} делает: {dog.sound()}")
print(f"{cat.name} делает: {cat.sound()}")