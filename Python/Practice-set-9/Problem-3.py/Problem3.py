#Program to generate multiplication tables from 2 to 20 and 
#write it to different files. Place these files in folder for 13 year old

def printTable(n):
    with open(f"table-{n}.txt", "w") as f:
        for i in range(1, 11):
            table = n*i
            f.write(f"{n} * {i} = {table}\n")
            
for n in range(2, 21):
    printTable(n)