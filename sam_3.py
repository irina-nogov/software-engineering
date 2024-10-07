import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

min_one = min(one)
max_one = max(one)
min_two = min(two)
max_two = max(two)
min_three = min(three)
max_three = max(three)

triangle1 = [max_one, max_two, max_three]
triangle2 = [min_one, min_two, min_three]

def squareTriangle(sides):
    a, b, c = sides
    s = (a + b + c) / 2
    square = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return square
square_triangle1 = squareTriangle(triangle1)
square_triangle2 = squareTriangle(triangle2)


print("Площадь треугольника с максимальными элементами:", square_triangle1)
print("Площадь треугольника с минимальными элементами:", square_triangle2)