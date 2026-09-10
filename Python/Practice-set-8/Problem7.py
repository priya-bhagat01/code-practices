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

def rem(l, word):
    p = []
    for item in l:
        if not(item == word):
            p.append(item.strip(word))
    return p

l = ["Harry", "Rohan", "Shubham", "an"]
print(rem(l, "an"))