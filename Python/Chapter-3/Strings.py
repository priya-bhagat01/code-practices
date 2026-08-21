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