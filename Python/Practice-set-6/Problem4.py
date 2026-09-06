#Program to find whether given username contains less than 10 characters or not

username = input("Enter a username: ")
length = len(username)

if(length < 10):
    print("Your username contains less than 10 character")
else:
    print("Your username contains more than 10 characters")