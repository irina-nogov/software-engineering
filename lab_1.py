#Создаем класс "Car"
class Car:
#Определяем атрибуты производитель и модель
    def __init__(self, make, model):
        self.make = make #Присваеваем производителя объекту
        self.model = model #Присваеваем модель объекту
# Создаем объект класса "Car" c производителем "Toyota" и моделью "Corolla"
my_car = Car('Toyota', 'Corolla') # Создаем объект my_car класса "Car" с указананными атрибутами