#Can you change values inside list which is contained in set s?
#s = {8, 7, 12, "Priya", [1,2]}

#No we can't,
# 1. We can't include a list in set because lists are mutable and not hashable
#an object is hashable if it has a 
#hash value that never changes during its entire lifetime
#Instead use tuple ()
# 2. If we use tuple, we can't change value inside set, to change 
# remove the old tuple and add new tuple
s = {8, 7, 12, "Priya", (1, 2)}
s.remove((1, 2))
s.add((1, 3))
print(s)