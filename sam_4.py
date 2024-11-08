# Создаем класс декоратора
class MultiplyByTwoDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs) * 2
        return result

# Создаем две функции, которые будут использовать наш декоратор
@MultiplyByTwoDecorator
def add(a, b):
    return a + b

@MultiplyByTwoDecorator
def multiply(a, b):
    return a * b

# Тестируем функции
print(add(3, 4)) 
print(multiply(3, 4))