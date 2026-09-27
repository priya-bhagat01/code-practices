#Create class "Programmer" for storing information of few programmers working at microsoft 

class Programmer:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def getInfo(self):
        print(f"Hi, My name is {self.name}, I work in Microsoft as {self.role}, and I earn {self.salary}")

priya = Programmer("Priya", "Software developer", "1500000")
priya.getInfo()