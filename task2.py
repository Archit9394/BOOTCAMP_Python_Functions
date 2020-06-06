# 2. 	Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
# Expected Output:
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

string_1="Consult Add"
upper=0
lower=0
for i in string_1:
    if (ord(i)>=65 and ord(i)<=90):
        upper+=1
    elif(ord(i)>=97 and ord(i)<=122):
        lower+=1

print ("No. of Upper case Characters :",upper)
print ("No. of Lower case Characters :",lower)