#Function to remove given word from list and strip it at same time
list = ["Rohan", 7, False, "Mango", 8.3]

n = input("Enter name you want to remove: ")

def removeWord(n):
    if(n in list):
        list.remove(n)
        print(list)
    else:
        print(f"{n} not found in list")

removeWord(n)