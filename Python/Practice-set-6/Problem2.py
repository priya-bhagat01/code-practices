#Program to find out whether student has passed or failed if it requires 
#Total of 40% and atleast 33% in each subject to pass. 
# Assume 3 subjects and take marks as input from user

studentMarks1 = int(input("Enter your Maths marks: "))
studentMarks2 = int(input("Enter your Physics marks: "))
studentMarks3 = int(input("Enter your Chemistry marks: "))
totalMarks = studentMarks1 + studentMarks2 + studentMarks3
percentage = (totalMarks/300)*100

if(studentMarks1 > 33):
    print("You are pass in Maths")

if(studentMarks2 > 33):
    print("You are pass in Physics")

if(studentMarks3 > 33):
    print("You are pass in Chemistry")

if(totalMarks > 40 and studentMarks1 > 33 and studentMarks2 > 33 and studentMarks3 > 33):
    print("Congratulations you are passed")
    print("Your percentage is:", percentage)