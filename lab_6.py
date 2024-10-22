with open('t1.txt', 'a+') as f:
    f.write('\n Sovsem chyt-chyt')

with open('t1.txt', 'r') as f:
    result = f.readlines()
    print(result)