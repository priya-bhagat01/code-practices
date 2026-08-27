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