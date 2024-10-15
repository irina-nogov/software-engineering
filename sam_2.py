def dele(kor, a):
    if a in kor:
        aInd = kor.index(a)
        return kor[:aInd] + kor[aInd + 1:]
    return kor

print(dele((1, 2, 3), 1))
print(dele((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(dele((2, 4, 6, 6, 4, 2), 9))