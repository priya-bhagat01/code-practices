#String is data type in python
#It is a sequence of characters enclosed in single quotes, double quotes, or triple quotes.
#Strings are immutable, meaning they cannot be changed after they are created.
a = 'Hello, World!'  # Single quotes
b = "Hello, World!"  # Double quotes
c = '''Hello, World!'''  # Triple quotes

name = "Priya" 
length = len(name)  # Gives Length of the string
print(length)  # Output: 5

short_name = name[0:3]  # Starts from index 0 to 2 (3 is not included)
print(short_name)  # Output: Pri

character1 = name[1]  # Accessing the first character of the string
print(character1)  # Output: r

#Negative indexing starts from the end of the string
character2 = name[-1]  # Accessing the last character of the string
print(character2)  # Output: a
print(name[-4: -1])  # Output: riy
#corresponding to above example, -4 is 1 and 1 is -4, -3 is 2 and 2 is -3, -2 is 3 and 3 is -2, -1 is 4 and 4 is -1
print(name[1:4])  # Output: riy

print(name[:]) # Output: Priya (prints the whole string)
print(name[:4]) # Output: Priy (prints from start to index 3)
print(name[1:]) # Output: riya (prints from index 1 to end)
