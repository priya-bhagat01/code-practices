#Function that converts inches to cms
#1 inch = 2.54 cm OR 1 inch = 127/50 cm

n = int(input("Enter number in inch: "))

def inchToCm(n):
    return 127/50*n
print(f"The measurment of {n} inches is {inchToCm(n)} cm")