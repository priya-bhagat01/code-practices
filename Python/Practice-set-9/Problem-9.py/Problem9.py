#Program to find out whether file is identical & matches content of another file

with open("Problem-9.py/File1.txt") as f:
    content1 = f.read()

with open("Problem-9.py/File2.txt") as f:
    content2 = f.read()

if content1 == content2:
    print("Yes these files are identical")

else:
    print("Yes these files are not identical")