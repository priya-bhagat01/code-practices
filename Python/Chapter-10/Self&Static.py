#Self Parameter
#Self refers to instance of class. It is automatically passed with function call from objects
#harry.getSalary() #here self is harry
#Equivalent to Employee.getSalary(harry) 
#function getSalary() is defined:
#class Employee:
#   company = "Google"
#   def getSalary(self):
#       print("Salary is not there")

class Employee:
    language = "Python"
    salary = 1200000

    # def getInfo(): 
    #     print(f"The language is {language} and the salary is {salary}")
    # This is wrong because 
    
    def getInfo(self): 
        print(f"The language is {self.language} and the salary is {self.salary}")

harry = Employee()
harry.language = "JavaScript"
print(harry.language, harry.salary)

harry.getInfo()
#This translates to Employee.getInfo(harry) 
#here harry is parameter but we haven't gave any in function thus it gives error so we use self



#Static method
#Sometimes we need function that does not use self parameter
#We can define Static method like this:
#@Staticmethod #decorator to mark greet as static method
#def greet:
#   print("Hello User")
class Employee:
    language = "Python"
    salary = 1200000
    
    def getInfo(self): 
        print(f"The language is {self.language} and the salary is {self.salary}")

    # def greet():  #This will show error because it does not have parameter but also doesnt need one
    #     print("Good Morning")

    @staticmethod
    def greet():
        print("Good Morning")

harry = Employee()
harry.language = "JavaScript"
print(harry.language, harry.salary)
harry.greet()
harry.getInfo()