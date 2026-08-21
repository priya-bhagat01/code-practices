#input function is used to take input from user
name = input("Enter your name: ")
print("Hello, " + name + "!")

a = input("Enter a number: ")
b = input("Enter another number: ")
print("Number a is:", a)
print("Number b is:", b)
print("Sum is:", a +b)  # This will concatenate the strings instead of adding numbers

#Number and strings cannot be added directly. We need to convert the input strings to integers or floats before performing arithmetic operations.
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print("Number a is:", a)
print("Number b is:", b)
print("Sum is:", a + b)