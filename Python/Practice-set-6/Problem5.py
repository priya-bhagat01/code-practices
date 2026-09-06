#Program which finds out whether given name is present in list or not
fruits = ["Apple", "Banana", "Orange", "Kiwi", "Mango"]

fruit = input("Enter a fruit name: ")

if(fruit in fruits):
    print(fruit, "is in list")
else:
    print(fruit, "is not in list")