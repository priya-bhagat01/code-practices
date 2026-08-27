marks = {
    "Priya": 95,
    "Rohan": 56,
    "Soham": 22
}

print(marks, type(marks))
print(marks["Rohan"])

#Methods of dictionaries
# .items returns list of key,value tuples
print(marks.items())

# .keys returns list of containing keys
print(marks.keys())

# .update updates dictionary with supplied key-value pairs
a = marks.update({"Rohan":55})
print(marks)

# .get returns value of specified key
print(marks.get("Priya"))

#Difference between marks.get and marks[] is 
#When marks.get key doesn't exist it gives none
print(marks.get("Siya"))

#When marks[] key doesn't exist it gives error
#print(marks["Siya"])

# .copy copies the dictionaries 
# .clear clears everything
#print(marks.clear())

# .fromkeys creates new dictionary 
keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys, 0)
print(new_dict) #Takes keys a, b, c with values 0

# .pop removes specified key and returns value, if not found default or keyerror is raised
value = marks.pop("Priya", 'default_value')
print(value)

# .popitem removes and returns key value pair, returnd in (last-in, first-out) order
item = marks.popitem()
print(item)