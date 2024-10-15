def countOften(num):
   numCount = {}
   for i in num:
       numCount[i] = numCount.get(i, 0) + 1
   oftenCommon = sorted(numCount.items(), key=lambda x: x[1], reverse=True)[:3]
   result = {key: value for key, value in sorted(oftenCommon)}
   return result
str=input()
print(countOften(str))

def mostNum(num):
    return max(set(num), key=num.count)
res = tuple(str)
print(mostNum(list(res)))