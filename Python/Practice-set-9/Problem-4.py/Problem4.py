#File contains word "Donkey" multiple times.
#Write program which replace this word with ###### by updating same file 

word = "Donkey"
word2 = "donkey"

with open("Problem-4.py/File.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######").replace(word2, "######")

with open("Problem-4.py/File.txt", "w") as f:
    f.write(contentNew)