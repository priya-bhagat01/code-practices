#Program to find out line number where python is present from quest 6

with open("Problem-7.py/Log.txt") as f:
    lines = f.readlines()

lineNo = 1
for line in lines:
    if("python" in line):
        print(f"Yes Python is present. Line no: {lineNo}")
        break
    lineNo += 1
else:
    print("No python is not present")