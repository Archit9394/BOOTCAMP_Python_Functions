# 9. Write a function called showNumbers that takes a parameter called limit.
# It should print all the numbers between 0 and limit with a label to identify
# the even and odd numbers. 
# Example: If the limit is 3 , it should print:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD

limit=3
def showNumbers(max_num):
    for i in range(0,max_num+1):
        if(i%2==0):
            print(i, "EVEN")
        elif(i%2==1):
            print(i, "ODD")

showNumbers(limit)