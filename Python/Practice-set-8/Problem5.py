#Write python function to print first n lines of following pattern:
'''
***
**
*
'''

n = int(input("Enter number: "))
i = 0

def starPattern(i, n):
    while i < n:
        print("*"* (n - i))
        i += 1
starPattern(i, n)