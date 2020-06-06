# 13. Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
# Goal : Turn [1,2,3,4,5,6,7] to 1234567 

import operator
from functools import reduce
list1=[[1,2,3],[4,5,6],[7,8,9]]

reduced_list=reduce(operator.add,list1)
print (reduced_list)

str1=""
for i in reduced_list:
    str1+=str(i)

print (int(str1))