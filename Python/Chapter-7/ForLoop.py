#A for loop is used to iterate through sequence like list, tuple, or string [iterables]
#Syntax:
#l = [1, 7, 8]
#   for item in l:
#       print(item) #prints 1, 7, 8

#for loop with list
l = [1, 4, 6, 234]
for i in l:
    print(i)

#for loop with tuple
t = (6, 231, 75)
for i in t:
    print(i)

#for loop with string
s = "Harry"
for i in s:
    print(i)

for i in range(7):
    print(i) #prints 0 to 6

#Range function in python
#range() function in python is used to generate sequence of number

#We can also specify start, stop & step-size as follows:
#range(start, stop, step_size)
for i in range(0, 100, 4): #step size is how much you want to skip
    print(i)

#For loop with else
#Optional else can be used with for loop
#if code is to be executed when loop exhausts
l = [1, 7, 8]
for item in l:
    print(item)
else:
    print("done")