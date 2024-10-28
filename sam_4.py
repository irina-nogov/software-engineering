class Animal:
    def __init__(self, name):
        self._name = name  #

    def sound(self):
        pass

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name


class Dog(Animal):
    def sound(self):
        return "Гав-гав!"


class Cat(Animal):
    def sound(self):
        return "Мяу!"



dog = Dog("Собака")
cat = Cat("Кот")


print(f"{dog.get_name()} делает: {dog.sound()}")
print(f"{cat.get_name()} делает: {cat.sound()}")


cat.set_name("Котик")
print(f"{cat.get_name()} делает: {cat.sound()}")