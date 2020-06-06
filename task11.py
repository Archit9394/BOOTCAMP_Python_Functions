# 11. Write a program which can map() and filter() to make a list whose elements
# are square of even number in [1,2,3,4,5,6,7,8,9,10]
# Hints: Use map() to generate a list.
#      	     Use filter() to filter elements of a list
#             Use lambda to define anonymous functions

list1=[]
for i in range(1,11):
    list1.append(i)

square=lambda i:i*i

def even(i):
    if (i%2==0):
        return True
    else:
        return False

a=map(square,list1)

b=filter(even,list(a))
print (list(b))