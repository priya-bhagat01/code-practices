#Can you change self parameter inside class to something else
#(say "Priya"), Try changing self to "slf" or "Priya" and see effects

#Yes it works, it can be anything

class Programmer:
    def __init__(slf, name, role, salary):
        slf.name = name
        slf.role = role
        slf.salary = salary

    def getInfo(slf):
        print(f"Hi, My name is {slf.name}, I work in Microsoft as {slf.role}, and I earn {slf.salary}")

priya = Programmer("Priya", "Software developer", "1500000")
priya.getInfo()

#OR 

class Programmer:
    def __init__(Priya, name, role, salary):
        Priya.name = name
        Priya.role = role
        Priya.salary = salary

    def getInfo(Priya):
        print(f"Hi, My name is {Priya.name}, I work in Microsoft as {Priya.role}, and I earn {Priya.salary}")

priya = Programmer("Priya", "Software developer", "1500000")
priya.getInfo()