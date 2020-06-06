# 6. Define a function that can receive two integral numbers
# in string form and compute their sum and print it in console.

x=input("Enter first number:")
y=input("Enter second number:")
def sum(first,second):
    total=int(first)+int(second)
    return total

x=sum(x,y)
print (x)