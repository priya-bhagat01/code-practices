#Tuples is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
#Tuples are immutable, meaning that you cannot change, add, or remove items after the tuple has been created. Tuples are defined by enclosing the elements in parentheses ().

a = () #Empty tuple
b = (1,) #Tuple with one element needs a trailing comma to differentiate it from a regular integer in parentheses.
c = (1, 2, 3, 4, 5) #Tuple with multiple elements

#Tuples methods
a = (1, 2, 3, 4, 5)
print(a.count(2))  # Output: 1, counts the number of occurrences of the specified value in the tuple
print(a.index(3))  # Output: 2, returns the index of the first occurrence of the specified value in the tuple

#Operations on Tuples
a = (1, 2, 3)
b = (4, 5, 6)
c = a + b  # Concatenation of tuples
print(c)  # Output: (1, 2, 3, 4, 5, 6)

d = a * 2  # Repetition of tuples
print(d)  # Output: (1, 2, 3, 1, 2, 3)

print(2 in a)  # Output: True, checks if the value is present in the tuple

print(len(a))  # Output: 3, returns the number of elements in the tuple

print(min(a))  # Output: 1, returns the smallest element in the tuple
print(max(a))  # Output: 3, returns the largest element in the tuple

sliced = a[1:3]  # Slicing the tuple
print(sliced)  # Output: (2, 3), returns a new tuple containing the elements from index 1 to index 2 (3 is not included)

d , b , c = a  # Tuple unpacking
print(d , b , c)  # Output: 1 2 3