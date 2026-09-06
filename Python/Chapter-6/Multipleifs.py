#Elif in python means else if An if statement can be chained together
#with alot of these elif statements followed by else statement
#There can be any number of elif statements
#Last else is executed only if all conditions in side elifs fail

#elifs ladder
a = int(input("Enter your age: "))

#If statement1
if(a % 2 == 0):
    print("a is even")
else:
    print("a is odd")

#If statement 2
if(a >= 18):
    print("You are above age of consent")
elif(a < 0):
    print("You are entering negative invalid age")
elif(a = 0):
    print("You are entering 0 invalid age")
else:
    print("You are below age of consent")