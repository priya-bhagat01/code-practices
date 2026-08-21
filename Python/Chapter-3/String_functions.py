#len function is used to get the length of the string
name = "Priya"
print(len(name))  # Output: 5

#String.endswith() method is used to check if the string ends with a specified suffix
name = "Priya"
print(name.endswith("ya"))  # Output: True

#String.startswith() method is used to check if the string starts with a specified prefix
name = "Priya"
print(name.startswith("Pr"))  # Output: True

#String.capitalize() method is used to capitalize the first character of the string
name = "priya"
print(name.capitalize())  # Output: Priya

#String.upper() method is used to convert all characters of the string to uppercase
name = "priya"
print(name.upper())  # Output: PRIYA

#String.lower() method is used to convert all characters of the string to lowercase
name = "PRIYA"
print(name.lower())  # Output: priya

#String.title() method is used to convert the first character of each word in the string to uppercase
name = "priya bhagat"
print(name.title())  # Output: Priya Bhagat

#String.strip() method is used to remove any leading and trailing whitespace characters from the string
name = "   Priya   "
print(name.strip())  # Output: Priya

#String.zfill() method is used to pad the string with zeros on the left until it reaches the specified width
number = "42"
print(number.zfill(5))  # Output: 00042

#String.replace() method is used to replace a specified substring with another substring in the string
name = "Priya Bhagat"
print(name.replace("Bhagat", "Sharma"))  # Output: Priya Sharma

#String.find() method is used to find the index of the first occurrence of a specified substring in the string
name = "Priya Bhagat"
print(name.find("Bhagat"))  # Output: 5