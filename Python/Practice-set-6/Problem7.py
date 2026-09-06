#Program to find out whether given post is talking about "Harry" or not

post = input("Enter the post: ")

if("Harry".lower() in post.lower()): #lower converts both and compares so it gives all harry, HArry, haRry
    print("This post is talking about harry")
else:
    print("This post is not talking about harry")