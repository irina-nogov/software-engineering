def passT(inpTuple: tuple, passId: int) -> tuple:
   startIndex = -1
   finishIndex = len(inpTuple)
   k = 0

   for i in range(len(inpTuple)):
       if passId == inpTuple[i]:
           startIndex = i
           k += 1
           break
   if k != 0:
       for i in range(startIndex + 1, len(inpTuple)):
           if passId == inpTuple[i]:
               finishIndex = i + 1
               break

   if startIndex != -1:
       return inpTuple[startIndex:finishIndex]
   else:
       return ()
print(passT((1, 2, 3), 8))
print(passT((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(passT((1, 2, 8, 5, 1, 2, 9), 8))