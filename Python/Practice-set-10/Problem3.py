#Create class with class attribute a;
#create object from it and set "a" directly using object a = o. 
#Does this change class attribute?

class demo:
    a = 4

o = demo()
print(o.a)

o.a = 0
print(o.a)

print(demo.a)

#The value of class attribute hasn't changed, just an instance attribute is set so it prints instance
#But class attributes value remains what it was