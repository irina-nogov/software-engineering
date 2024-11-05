class Irina:
    slots = ["name"]

    def __init__(self, name):
        if name == 'Ирина':
            self.name = f"Да, я {name}"
        else:
            self.name =f"Я не {name}, а Ирина"

person1 = Irina('Мария')
person2 = Irina('Ирина')
print(person1.name)
print(person2.name)

person2.surname='Ноговицина'