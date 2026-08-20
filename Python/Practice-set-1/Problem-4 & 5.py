#Write python program to print contents of directory using os module
# Label the program written in problem 4 with comments

#import module
import os

#Get current working directory
working_directory = "."

#List all files and directories in current working directory
contents = os.listdir(working_directory)

#print the contents of the directory
print(contents)
