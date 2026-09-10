#Recursive function to calculate sum of first n natural numbers
#sum of n natural numbers = n*(n+1)/2

n = int(input("Enter number till you want sum of: "))

def sumOfNumbers(n):
    return n*(n + 1)/2
print(f"Sum of {n} natural numbers is {sumOfNumbers(n)}")

'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(n) = 1 + 2 + 3 +....+ n-1 + n

sum(n) = sum(n-1) + n
'''

def sum(n):
    if n == 1:
        return 1
    return sum(n-1) + n
print(f"Sum of {n} natural numbers is {sumOfNumbers(n)}")