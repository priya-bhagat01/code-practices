#Program to find sum of first n natural numbers using while loop
n = int(input("Enter number for first natural numbers: "))
formula = n*(n+1)/2
i = 0
while i < n:
    print("n(n+1)/2 =", formula)
    i += 1
    break

#OR
sum = 0
while i <= n:
    sum += i
    i += 1

print(sum)