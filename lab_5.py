# Определение общего класса Shape
class Shape:
    def area(self):
        pass

# Определение класса Rectangle, унаследованного от Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
# Метод для подсчета плдощади прямоугольника
    def area(self):
        return self.width * self.height

#Определение класса Circle, унаследованного от Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
# Метод для подсчета площади круга
    def area(self):
        return 3.14 * self.radius * self.radius
# Создание экземпляров классов Rectangle и Circle
rectangle = Rectangle(2, 10)
circle = Circle(7)

# Помещение фигур в массив
shapes = [rectangle, circle]

# Вывод площади каждой фигуры в массиве
for shape in shapes:
    print(shape.area())