#Program using functions to find greatest of three numbers

n1 = int(input("Enter number: "))
n2 = int(input("Enter number: "))
n3 = int(input("Enter number: "))

def findGreatest():
    if(n1 >= n2 and n1 >= n3):
        print("Greatest number is: ", n1)
    elif(n2 >= n1 and n2 >= n3):
        print("Greatest number is: ", n2)
    elif(n3 >= n2 and n3 >= n1):
        print("Greatest number is: ", n3)
    return findGreatest
findGreatest()