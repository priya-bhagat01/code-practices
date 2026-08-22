#Check that tuple type cannot be changed in python
x = (1, 2, 3)
print(type(x))
x[0] = 5  #This would raise an error because tuples are immutable