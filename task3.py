# 3.Create a function that takes a list and returns a new list 
#   with unique elements of the first list.

list1=[10,20,30,20,30,40]

def unique_list(list1):
    list_set=set(list1)
    list2=list(list_set)
    return list2
x= unique_list(list1)
print (x)