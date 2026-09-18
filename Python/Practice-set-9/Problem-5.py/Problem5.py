#Repeat program 4 for list of such words to be censored

words = ["donkey", "walked", "the"]

with open("Problem-5.py/File.txt", "r") as f:
    content = f.read()

for w in words:
    content = content.replace(w, "######")

with open("Problem-5.py/File.txt", "w") as f:
    f.write(content)