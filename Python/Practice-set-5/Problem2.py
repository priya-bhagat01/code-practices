#Program to input eight numbers from user and display all unique numbers once

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))
e = int(input("Enter number 5: "))
f = int(input("Enter number 6: "))
g = int(input("Enter number 7: "))
h = int(input("Enter number 8: "))

my_set = {a, b, c, d, e, f, g, h}
print(my_set)

#OR

s = set()
n = input("Enter number:")
s.add(int(n))
n = input("Enter number:")
s.add(int(n))
n = input("Enter number:")
s.add(int(n))
n = input("Enter number:")
s.add(int(n))
n = input("Enter number:")
s.add(int(n))
n = input("Enter number:")
s.add(int(n))
n = input("Enter number:")
s.add(int(n))
n = input("Enter number:")
s.add(int(n))

print(s)