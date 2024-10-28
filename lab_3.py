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

class ElectricCar(Car): #  конструкторе класса ElectricCar вызывается конструктор родительского класса Car с помощью super() и добавляется атрибут battery_capacity.
    def __init__(self, make,model,battery_capacity):
        super().__init__(make,model)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f'Charging the {self.make} {self.model} with {self.battery_capacity} kWh')

#Создается экземпляр my_electric_car класса ElectricCar с параметрами 'Tesla', 'Model S', 75.
my_electric_car = ElectricCar('Tesla', 'Model S', 75)
# Вызывается метод drive() для экземпляра my_electric_car, который выводит информацию о том, что машина едет.
my_electric_car.drive()
#Вызывается метод charge() для экземпляра my_electric_car, который выводит информацию о зарядке машины.
my_electric_car.charge()