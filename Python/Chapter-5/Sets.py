e = set() #empty set, {} is used for empty dictionaries
s = {1, 8, 2, 3}

#set method

# .add adds to the set
s.add(5)
print(s)

# len finds length of set
print(len(s))

# .remove removes value 
a = s.remove(8)
print(s)

# .pop removes element and returns element removed 
b = s.pop()
print(b)

# union, returns new set with all items from both set
# intersection, return new set which contains only common
s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1.union(s2))
print(s1.intersection(s2))