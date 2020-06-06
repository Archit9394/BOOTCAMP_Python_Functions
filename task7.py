# 7.Define a function that can accept two strings as input and print the string with
# maximum length in console. If two strings have the same length, then the function
# should print all strings line by line.


str_1=input("Enter first string:")
str_2=input("Enter second string:")

def max_length(string1,string2):
    len1=len(string1)
    len2=len(string2)
    if (len1>len2):
        print(string1)
    elif(len1>len2):
        print(string2)
    else:
        print(string1)
        print(string2)

x=max_length(str_1,str_2)