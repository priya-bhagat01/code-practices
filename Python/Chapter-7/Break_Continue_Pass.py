#Break 

#It is used to come out of loop when encountered
#It instructs program to exit loop now
for i in range(0, 80):
    print(i)
    if i == 3:
        break #Exit loop rn

#Continue

#It is used to stop current iteration of loop & continue with next one. 
#It instructs program to skip this iteration
for i in range(4):
    print("printing")
    if i == 2:
        continue #iteration is skipped
    print(i)

#Pass

#It is pull statement in python
#It instructs to do nothing
l = [1, 7, 8]
for item in l:
    pass #without pass, program will throw error