#RAM - random access memory is volatile & all its contents are lost once program terminates 
#In order to persist data forever, we use files

#File is data stored in storage device
#Python program can talk to file by reading & writing content from it

#Type of files:
#Text files (.txt, .c, etc)
#Binary files (.jpg, .dat, etc)
#Python has lot of function for reading, updating & deleted files

#Opening file
#Python has open() function for opening files
#It takes 2 parameters, filename & mode
#open("filename", "mode of opening(read mode)")
#open("this txt", "v")

#Reading file in python

#Open file in read mode 
#f = open("this.txt", "r")

#Read its content
#text = f.read()

#Print its content 
#print(text)

#Close the file
#f.close()

f = open("file.txt")
data = f.read()
print(data)
f.close()