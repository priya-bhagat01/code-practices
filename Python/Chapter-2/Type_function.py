#type function is used to check the datatype of variable
a = 1
print(type(a))  # Output: <class 'int'>
b = 5.22
print(type(b))  # Output: <class 'float'>
c = "Hello"
print(type(c))  # Output: <class 'str'>
d = True
print(type(d))  # Output: <class 'bool'>
e = None
print(type(e))  # Output: <class 'NoneType'>

#number and strings are interchangeable in python. we can convert number to string and string to number using str() and int() functions respectively.
num = 10
print(type(num))  # Output: <class 'int'>
num_str = str(num)
print(type(num_str))  # Output: <class 'str'>
num_back = int(num_str)
print(type(num_back))  # Output: <class 'int'>