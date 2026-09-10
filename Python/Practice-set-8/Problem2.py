#Program using function to convert Celcius to Fahrenheit
'''
C = (x - 0)/100 = F = (x - 32)/180 = K = (x - 273)/100

C/5 = (F - 32)/9 = (K - 273)/5
9/5C + 32 = F
'''

C = int(input("Enter temperature in celcius: "))

def CtoF(C):
    return 9/5*C + 32

print(f"The temp of {C} celcius is {CtoF(C)} Fahrenheit")