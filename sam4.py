stroka = input()
print(' 1. Длина предложения: ', len(stroka), "\n", '2. Перевод в нижний регистр: ', stroka.lower(), "\n", '3. Количество гласных (a, e, i, o, u):', stroka.count('a')+stroka.count('e')+stroka.count('i')+stroka.count('o')+stroka.count('u'), "\n", '4. Замена слов "ugly" на "beauty": ', stroka.replace("ugly","beauty"))
if stroka[:3]=='The' and stroka[-3:]=='end':
    print(" 5. Предложение начинается с The и заканчивается на end")
elif stroka[:3]=='The' and stroka[-3:]!='end':
    print(" 5. Предложение начинается с The и не заканчивается на end")
elif stroka[:3]!='The' and stroka[-3:]=='end':
    print(" 5. Предложение не начинается с The и заканчивается на end")
else:
    print(" 5. Предложение не начинается с The и не заканчивается на end")
