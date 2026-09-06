#IF ELSE & ELIF in python are multiway decision taken by our program 
#due to certain conditions in our code
#Syntax:
condition1 = 0
condition2 = 0
if(condition1): #if condition1 is true
    print("yes")
elif(condition2): #if condition2 is true
    print("no")
else:               #otherwise
    print("maybe")

#Code example:
a = 22
if(a > 9):
    print("greater")
else: 
    print("lesser")

#Program to print yes when age entered by user is greater than or qual to 18
b = int(input("Enter your age:"))
if(b >= 18):
    print("You are above age of consent")
elif(b < 0):
    print("You are entering an invalid age")
else:
    print("You are below age of consent")