#Program to make copy of text file "this.txt"

with open("Problem-8.py/this.txt") as f:
    content = f.read()

with open("Problem-8.py/this-copy.txt", "w") as f:
    f.write(content)