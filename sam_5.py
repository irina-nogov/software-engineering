from triangle_area import calculate_area

if __name__ == "__main__":
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    c = float(input("Введите длину стороны c: "))

    area = calculate_area(a, b, c)
    print(f"Площадь треугольника: {area}")