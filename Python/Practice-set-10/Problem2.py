#Write class "calculator" capable of finding square, cube and square root of number

a = int(input("Enter a number: "))

class calculator:
    def findSquare(self, a):
        print(f"square of a = {a ** 2}")
    
    def findCube(self, a):
        print(f"cube of a = {a ** 3}")
    
    def findSquareRoot(self, a):
        formula = a ** 0.5
        rounding = round(formula, 2)
        print(f"square root of a = {rounding}")

calculation = calculator()
calculation.findCube(a)
calculation.findSquare(a)
calculation.findSquareRoot(a)