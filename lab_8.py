import math

if __name__ == "__main__":
    number = float(input("Введите число: "))
    root = math.sqrt(number)
    sin_value = math.sin(number)
    cos_value = math.cos(number)

    print(f"Корень числа: {root}")
    print(f"Синус числа: {sin_value}")
    print(f"Косинус числа: {cos_value}")