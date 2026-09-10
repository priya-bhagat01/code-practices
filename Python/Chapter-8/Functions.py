#function is group of statements performing specific tasks
#When program gets bigger in size & its complexity grows, it gets difficult for program 
#to keep track on which piece of code is doing  what
#Function can be reused by programmer in given program


#Syntax:
def func1():
    print("hello")
func1() #this is called function call


#Program to greet user with "Good Day" using function
def greet():
    print("Good Day")
greet() 

#Types of function

#Built in function: Already present in python
print("A")
#len()
#range(1, 11)

#User defined function: Defined by user
func1()

#Function with arguments
#Function can accept some values it can work with. 
#We can put these values of parentheses
#Function can return values as shown

def greet(name):
    gr = "hello, " + name
    return gr
a = greet("Harry")
print(a)

def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)
    return goodDay

a = goodDay("Harry", "Thank You")
goodDay("Divya", "Thanks")

#Default parameter value

#We can have value as default argument in function
#If we specify name = "Stranger" in line containing def, 
#this value is used when no argument is passed

def greet(name = "stranger"):
    print("Hello, " + name)

greet() #name will be "stranger" in function body(default)
greet("Priya") #name will be "Priya" in function body(passed)

def goodday(name, ending = "Thank you"):
    print(f"Good day, {name}")
    print(ending)

goodday("Harry") #prints Good day, Harry, Thank you

