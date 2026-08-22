friends = ["Apple", "Orange", 5, 345.06, False, "Akash", "Rohan"]

print(friends[0])  # Output: Apple
friends[1] = "Banana"  # Changing the value at index 1
print(friends)  # Output: ['Apple', 'Banana', 5, 345.06, False, 'Akash', 'Rohan'] 
#We can't do the same with strings because strings are immutable in Python.

#List Methods
L1 = [1, 8, 7, 2, 21, 15]

L1.sort()  # Sorts the list in ascending order
print(L1)  # Output: [1, 2, 7, 8, 15, 21]

L1.reverse()  # Reverses the list
print(L1)  # Output: [21, 15, 8, 7, 2, 1]

L1.append(5)  # Adds an element to the end of the list
print(L1)  # Output: [21, 15, 8, 7, 2, 1, 5]

L1.insert(2, 10)  # Inserts an element at a specific index
print(L1)  # Output: [21, 15, 10, 8, 7, 2, 1, 5]

L1.pop()  # Removes the last element from the list
print(L1)  # Output: [21, 15, 10, 8, 7, 2, 1]

L1.remove(10)  # Removes the first occurrence of a specific value
print(L1)  # Output: [21, 15, 8, 7, 2, 1]