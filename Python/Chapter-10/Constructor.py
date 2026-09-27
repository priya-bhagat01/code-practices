#_init_() constructor
#It is also called Dunder method (which starts with underscore)
#_init_() is special method which is first run as soon as object is created
#_init_() method is also known as constructor
#It takes self-argument & can also take further arguments
#ex: class Employee:
#       def _init_(self,name):  (Auto call)
#           self.name = name
#       def getSalary(self):
#           ...
#    harry = Employee("Harry")

class Employee:
    language = "Python"
    salary = 1200000

    def __init__(self, name, salary, language):   #dunner method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
    
    def getInfo(self): 
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

harry = Employee("Priya", 40000000, "JavaScript")
#harry.name = "Harry"
print(harry.name, harry.salary, harry.language)
harry.greet()
harry.getInfo()

#rohan = Employee()