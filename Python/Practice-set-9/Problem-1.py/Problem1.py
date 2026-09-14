#Write program to read text from given file 'poems.txt' 
#and find out whether it contains the word 'twinkle'

with open("Problem-1.py/Poems.txt", "r") as f:
    text = f.read()
    if "twinkle" in text.lower():
        print("The following file contains the word twinkle")