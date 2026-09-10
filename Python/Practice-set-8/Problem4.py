#Recursive function to calculate sum of first n natural numbers
#sum of n natural numbers = n*(n+1)/2

n = int(input("Enter number till you want sum of: "))

def sumOfNumbers(n):
    return n*(n + 1)/2
print(f"Sum of {n} natural numbers is {sumOfNumbers(n)}")