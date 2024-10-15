def sumBol(num, bol):
    sumN = sum(num)
    return sumN > bol

print(sumBol((1, 2, 3, 4, 5), 7))
print(sumBol((2, 4, 3), 13))
print(sumBol((9, 6, 2, 8, 5, 5, 3, 11), 46))