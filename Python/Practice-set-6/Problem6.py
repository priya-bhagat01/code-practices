#Program to calculate grade of student from his marks from following schemes:
#90-100 => Ex, 80-90 => A, 70-80 => B, 60-70 => C, 50-60 => D, <50 => F

percentage = int(input("Enter your Percentage: "))

if(percentage >= 90):
    print("Excellent")
elif(percentage >= 80):
    print("A")
elif(percentage >= 70):
    print("B")
elif(percentage >= 60):
    print("C")
elif(percentage >= 50):
    print("D")
elif(percentage <= 50):
    print("F")