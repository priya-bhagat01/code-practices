#Recursion is function which calls itself
#It is used to directly use mathematical formula as function

'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 x 1
factorial(3) = 3 x 2 x 1
factorial(4) = 4 x 3 x 2 x 1
factorial(5) = 5 x 4 x 3 x 2 x 1
factorial(n) = n x (n-1)...x 3 x 2 x 1

factorial(n) = n x factorial(n - 1)
'''

n = int(input("Enter number: "))
def factorial(n):
    if(n == 0 or n == 1):
        #base condition which doesn't call function any further
        return 1
    else:
        return n*factorial(n-1) #function calling itself
print(f"factorial of this number is: {factorial(n)}")