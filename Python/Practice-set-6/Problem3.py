#Spam comment is defined as text containing following keywords:
#"Make a lot of money", "buy now", "subscribe this", "click this", 
# write program to detect these spams

word = """Are you ready to make a lot of money from your home? 
You do not want to miss this rare chance. 
Just buy now before our special deal ends today. 
Make sure you subscribe this channel for daily tips and updates. 
To get started right away, just click this link below and claim your reward!"""

if("make a lot of money" in word or "buy now" in word or "subscribe this" in word or "click this" in word):
    print("The following comment is spam, Beware of this")
else:
    print("This comment is clean!")

words = input("Enter a statement: ")

if "make a lot of money" in words:
    print("The following comment is spam, Beware of this")
elif "buy now" in words:
    print("The following comment is spam, Beware of this")
elif "subscribe this" in words:
    print("The following comment is spam, Beware of this")
elif "click this" in words:
    print("The following comment is spam, Beware of this")
else:
    print("This comment is clean!")