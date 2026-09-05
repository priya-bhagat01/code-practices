#Create empty dictionary. Allow 4 friends to enter their favourite language 
#as value and use key as their names. Assume names are unique

fav_language = {}
fav_language.update({input("Enter your name:"): input("Enter your favourite language:")})
fav_language.update({input("Enter your name:"): input("Enter your favourite language:")})
fav_language.update({input("Enter your name:"): input("Enter your favourite language:")})
fav_language.update({input("Enter your name:"): input("Enter your favourite language:")})
print(fav_language)