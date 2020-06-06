# 10. Write a program which can filter() to make a list whose elements are even number
#  between 1 and 20 ( both included)

list1=[]
for i in range(1,21):
    list1.append(i)
def filt(i):
        if(i%2==0):
            return True
        else:
            return False

filtered=filter(filt,list1)

for f in filtered:
    print (f)