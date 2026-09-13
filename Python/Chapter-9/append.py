#Append mode means adding to the end
st = "Hey, you are amazing"
f = open("myfile.txt", "a")
f.write(st)
f.close()

#when we run this on terminal, it keeps adding the string at the end depending on how many times
#we run this in terminal