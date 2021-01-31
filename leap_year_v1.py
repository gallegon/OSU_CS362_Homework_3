# Assignment 1
# Nicholai Gallegos
# Program asks user to input a year, then prints if the year entered is
# a leap year or not

# INSTRUCTIONS FOR RUNNING:
# run the command "python assign1.py"
# Enter an integer.  The program assumes a valid integer will be entered
# by the user. 
# The program will close after printing the result.

print("Is it a leap year?")

year = input("Enter a year to check: ");
isLeapYear = True;

if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 == 0:
			isLeapYear = True
		else:
			isLeapYear = False
else:
	isLeapYear = False

if isLeapYear == True:
	print(str(year) + " is a leap year!")
else:
	print(str(year) + " is NOT a leap year!")
