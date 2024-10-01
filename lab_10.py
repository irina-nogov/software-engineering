def triangle_area(base, height):
    return 0.5 * base * height


def rectangle_area(length, width):
    return length * width


if __name__ == "__main__":
    shape = input("Выберите фигуру (треугольник/прямоугольник): ").strip().lower()

    if shape == "треугольник":
        base = float(input("Введите основание треугольника: "))
        height = float(input("Введите высоту треугольника: "))
        area = triangle_area(base, height)
        print(f"Площадь треугольника: {area}")
    elif shape == "прямоугольник":
        length = float(input("Введите длину прямоугольника: "))
        width = float(input("Введите ширину прямоугольника: "))
        area = rectangle_area(length, width)
        print(f"Площадь прямоугольника: {area}")
    else:
        print("Неизвестная фигура")