import math

def calculate_area(a, b, c):
    s = (a + b + c) / 2  # Полупериметр
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # Формула Герона
    return area
