#Write program to fill in letter template with name and date
letter = '''
Dear <|NAME|>,
You are selected!
<|DATE|>
'''

print(letter.replace("<|NAME|>", input("Enter your name: ")).replace("<|DATE|>", input("Enter date: ")))