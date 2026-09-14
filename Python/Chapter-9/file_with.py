#With Statement
#Best way to open & close file automatically is with statement
#Open file in read mode using 'with', which automatically closes file
#with open("this.txt", "r") as f:
    #Read contents of file
    #text = f.read()
#Print contents
#print(text)

with open("file.txt", "r") as f:
    text = f.read()
print(text)