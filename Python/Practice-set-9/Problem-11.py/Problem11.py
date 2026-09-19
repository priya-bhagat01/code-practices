#Program to rename file to "renamed_by_python.txt"
#There are two ways to do this:

#1 is to import OS module to delete the old file 
#2 is to create a copy of old file and delete it manually

with open("Problem-11.py/old.txt") as f:
    content = f.read()

with open("Problem-11.py/renamed_by_python.txt", "w") as f:
    f.write(content)