# CSE 101 Lab 1 - Choongheon Lee (ID #109631572)

feet = int( input("Enter your height in whole feet: "))
inches = int( input("Enter your height in whole inches: "))
height = (feet * 12) + inches
over = height - 60
ideal = 110 + (over * 5)

print("Your ideal body weight is", ideal)
