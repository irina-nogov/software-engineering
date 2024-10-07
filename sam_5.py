list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

def createSet(list):
    counts = {}

    for num in list:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    result = set()

    for num, count in counts.items():
        result.add(num)
        for i in range(1, count):
            result.add(str(num) * (i + 1))
    return result

set_1 = createSet(list_1)
set_2 = createSet(list_2)
set_3 = createSet(list_3)

print(set_1)
print(set_2)
print(set_3)