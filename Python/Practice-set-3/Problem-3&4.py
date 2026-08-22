#Write program to detect double spaces in a string
name = "Priya is a good  girl  and she is a good  student"
print(name.find("  "))

#Write program to replace double spaces with single space
name = name.replace("  ", " ")
print(name) #Strings are immutable which means we cannot change the original string. We can only create a new string with the desired changes.