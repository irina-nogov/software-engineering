gradesList1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
gradesList2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
gradesList3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

def updateGrades(grades):
    updateGrades = [4 if a == 3 else a for a in grades if a != 2]
    return updateGrades
grades1 = updateGrades(gradesList1)
grades2 = updateGrades(gradesList2)
grades3 = updateGrades(gradesList3)

print(grades1)
print(grades2)
print(grades3)