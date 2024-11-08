# Создаем исключение
class ValueTooSmallError(Exception):
    pass

# Использование 1 исключения
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Невозможно разделить на ноль")
    if a < b:
        raise ValueTooSmallError("Значение «a» должно быть больше или равно значению «b».")
    return a / b

try:
    result = divide(5, 2)
    print(result)
except ZeroDivisionError as e:
    print(e)
except ValueTooSmallError as e:
    print(e)

# Использование 2 исключения
def calculate_square_root(num):
    if num < 0:
        raise ValueTooSmallError("Невозможно вычислить квадратный корень из отрицательного числа")
    return num ** 0.5

try:
    result = calculate_square_root(25)
    print(result)
except ValueTooSmallError as e:
    print(e)