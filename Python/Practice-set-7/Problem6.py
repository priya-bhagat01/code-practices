#Program to calculate factorial of given number using for loop
n = int(input("Enter number you want factorial of: "))

product = 1
for i in range(1, n+1):
    product = product * i

print(f"Factorial of {n} is {product}")