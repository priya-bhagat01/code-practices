#Syntax:
#while(condition)
#   Body of loop

#In while loop condition is checked first, 
#If it evaluates to true, body of loop is executed otherwise not

#If loop is enetered, process of (condition check & execution)
#is continued until condition because False

#If condition never become false, loop keeps getting executed

#Program to write 1 to 50
i = 1
while i < 51:
    print(i)
    i += 1

#Print content of list
l = [1, "Harry", False, "This", 20.0, "5"]

i = 0
while i < len(l):
    print(l[i])
    i += 1