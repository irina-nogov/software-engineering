#Создаем класс "Car"
class Car:
#Определяем атрибуты производитель и модель
    def __init__(self, make, model):
        self.make = make #Присваеваем производителя объекту
        self.model = model #Присваеваем модель объекту

    def drive(self): # Определяем метод drive
        print(f"Driving the {self.make} {self.model}") # Выводим сообщение о том, что мы ведем машину указанной марки и модели

# Создаем объект класса "Car" c производителем "Toyota" и моделью "Corolla"
my_car = Car("Toyota", "Corolla") # Создаем объект my_car класса "Car" с указананными атрибутами
my_car.drive() # вызываем метод drive для экземпляра my_car