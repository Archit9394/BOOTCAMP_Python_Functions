# 8.Define a function which can generate and print a tuple where the value are
#  square of numbers between 1 and 20.

list1=[]
def square():
    for i in range(1,21):
        list1.append(i**2)
    x=tuple(list1)
    return x
ans=square()
print (ans)