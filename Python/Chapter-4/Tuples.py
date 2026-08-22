#Tuples is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
#Tuples are immutable, meaning that you cannot change, add, or remove items after the tuple has been created. Tuples are defined by enclosing the elements in parentheses ().

a = () #Empty tuple
b = (1,) #Tuple with one element needs a trailing comma to differentiate it from a regular integer in parentheses.
c = (1, 2, 3, 4, 5) #Tuple with multiple elements

#Tuples methods
a = (1, 2, 3, 4, 5)
print(a.count(2))  # Output: 1, counts the number of occurrences of the specified value in the tuple
print(a.index(3))  # Output: 2, returns the index of the first occurrence of the specified value in the tuple