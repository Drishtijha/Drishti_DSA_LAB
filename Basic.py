# Electricity Bill 

unit = int(input("Enter electricity units: "))

if unit <= 100:
    bill = unit * 3
elif unit > 101 and unit <= 300:
    bill = unit * 4
else:
    bill = unit * 5

print("Electricity bill =", bill)


#Check even or odd number

n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")


#Find Largest and Smallest of 3 Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    largest = a
elif b > c:
    largest = b
else:
    largest = c
if a < b and a < c:
    smallest = a
elif b < c:
    smallest = b
else:
    smallest = c
print("Largest number:", largest)
print("Smallest number:", smallest)


#Grade of Student According to Marks\
marks = int(input("Enter student marks: "))

if marks >= 90 and marks <= 100:
    print("Excellent")
elif marks >= 70 and marks < 90:
    print("Very Good")
elif marks >= 60 and marks < 70:
    print("Good")
elif marks >= 50 and marks < 60:
    print("Fair")
elif marks >= 0 and marks < 50:
    print("Poor")
else:
    print("Invalid marks")
