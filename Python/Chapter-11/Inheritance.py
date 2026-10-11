#Inheritance is way of creating new dress from existing class 

#Syntax:

#class Employee: #Base class
    #code

#class Programmer(Employee): #Derived or child class
    #code

#We can use method & attributes of "Employee" in "Programmer"
#Also, we can overwrite or add new attributes & methods in "Programmer" class

class Employee:
    company = "ITC"

    def show(self):
        print(f"The name of employee is {self.name} and salary is {self.salary}")

# class Programmer:
#     company = "ITC Infotech"

#     def show(self):
#         print(f"The name of employee is {self.name} and salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and the person is good with {self.language} language")

#OR

class Programmer(Employee):
    company = "ITC Infotech"

    def showLanguage(self):
        print(f"The name is {self.name} and the person is good with {self.language} language")


a = Employee()
b = Programmer()

print(a.company, b.company)

#Types of inheritance
#Single Inheritance