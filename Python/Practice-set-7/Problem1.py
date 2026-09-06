#Program to print multiplication table of given number using for loop
number = int(input("Enter number: "))

for i in range(0, 11):
    print(number * i)

#OR
for i in range(1, 11):
    print(f"{number} X {i} = {number * i}")