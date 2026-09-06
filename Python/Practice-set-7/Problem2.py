#Program to greet all persons names stored in list 'l' and which starts with 'S'
l = ["Harry", "Soham", "Sachin", "Rahul"]

for name in l:
    if name.startswith("S"):
        print(f"Hello {name}, How are you")