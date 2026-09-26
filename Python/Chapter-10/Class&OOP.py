#Solving problem by creating object is one of most popular approaches in programming.
#This is called Object Oriented Programming(OOP)
#Concept focuses on using reusable code(DRY Principle)

#Class is blueprint for creating object
#Class is like blank form, and object is like filled form 
#Class contains info to create valid object 
#Syntax:
#class Employee: #Class name is written in pascal case
    #Methods and variables

class Employee: 
    language = "Py" #This is class attribute
    salary = 1200000

harry = Employee()
harry.name = "Harry" #This is object attribute
print(harry.name, harry.language)

#Here name is instance(object) attribute & salary & langauge are 
#class attribute as they directly belong to class