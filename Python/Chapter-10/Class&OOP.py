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

#Object is instantiation of class, When class is defined, template(info) is defined
#Memory is allocated only after object instantiation
#Object of given class can invoke methods available to it without revealing implementation
#detailed to user. Abstractions & Encapsulation

#Modelling problem in OOP's
#noun -> Class -> Employee
#Adjective -> Attributes -> name, age, salary
#Verb -> Methods -> getSalary(), increment()

#Class Attribute is attribute that belongs to class rather than particular object
#ex: class Employee:
#       company = "Google" #Specific to each class
#
#    harry = Employee() #Object Instantiation
#    harry.company
#    Employee.company = "YouTube" #Changing class attributes

#Instance Attribute is attribute that belongs to instance(object)
#ex: class Employee:
#       company = "Google" #Specific to each class
#
#    harry = Employee() #Object Instantiation
#    harry.name = "Harry"
#    harry.salary = "30K" #Adding Instance attributes

#Note: Instance attributes, take preference over class attributes during assignment & retrieval

#When looking up for harry.attribute it checks for the foll:
#   1)is attributes present in object?
#   2)is attributes present in class?