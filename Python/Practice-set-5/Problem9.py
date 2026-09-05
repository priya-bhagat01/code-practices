#Can you change values inside list which is contained in set s?
s = {8, 7, 12, "Priya", [1,2]}

#No we can't,
# 1. We can't include a list in set because lists are mutable and not hashable
#hashable means an object is hashable if it has a 
#hash value that never changes during its entire lifetime
# 2. Even if we could include list we won't be able to change 