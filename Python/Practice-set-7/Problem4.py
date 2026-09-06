#Program to find whether given number is prime or not
number = int(input("Enter number: "))

for i in range(2, number):
    if number % i == 0:
        print("Number is not prime")
        break #to break because without it repeats number is prime or not prime
    else:
        print("Number is prime")
        break