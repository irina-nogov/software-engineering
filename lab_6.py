def get_values(**kwargs):
    return list(kwargs.values())

def calculate_average(*args):
    return sum(args) / len(args) if args else 0

if __name__ == "__main__":
    values = get_values(a=10, b=20, c=30, d=40)
    average = calculate_average(*values)
    print(f'Среднее: {average}')
    