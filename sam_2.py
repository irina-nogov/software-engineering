def record_expense(filename):
    while True:
        expense_item = input("Введите название расхода (или 'отмена' для выхода): ")
        if expense_item.lower() == 'отмена':
            break
        expense_amount = input("введите данные расходов:")

        with open(filename, 'a', encoding='utf-8') as file:
            file.write(f"{expense_item}: {expense_amount}\n")

    print()
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())

filename = 'raskhod.txt'
record_expense(filename)
