#Function to give multiplication of given number

n = int(input("Enter number: "))
i = 1

def multiplicationTable():
    for i in range(1, 11):
        print(f"{n}x{i} = {n*i}")

multiplicationTable()