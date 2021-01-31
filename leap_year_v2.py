################################################################################ 
# File name: leap_year_v2.py
# Author: Nicholai Gallegos
# Due Date: 1/30/21
################################################################################

################################################################################
# Function name: isValidInput
# Parameters: input(string)
# Description: Determines if parameter [input] an integer equal to or greater
# than zero
# Return: TRUE if input is an integer >=0
#			 FALSE otherwise
################################################################################

def isValidInput(input):
	# try to convert user keyboard input to an integer
	try:
		input = int(input)
		
		# if it is an integer, see if it is atleast 0
		if input >= 0:
			return True
		else:
			print("Error: integer must be positive.")
			return False
	
	# catch exception if anything other than an integer is entered
	except:
		print("ValueError: invalid input")
		return False
		
################################################################################
# Function Name: getInput
# Parameters: None
# Description: Gets keyboard input from user, then calls isValidInput until 
# a valid integer is given.  Returns the input from keyboard as an integer.
# Return: an integer >= 0e
################################################################################
		
def getInput():
	# get initial input
	input = raw_input("Enter a year: ")
	inputValid = isValidInput(input)

	# loop until good input is given
	# this code block should not execute if good input was given initially
	while inputValid == False:
		input = raw_input("Enter a year: ")
		inputValid = isValidInput(input)
	
	return int(input)

################################################################################
# Function Name: isLeapYear
# Parameters: year(int)
# Description: Determines if year given is a leap year
# Return: TRUE if year is a leap year
# 			 FALSE if year is not a leap year
################################################################################

def isLeapYear(year):
	# conditions for leap year
	if year % 4 == 0:
		if year % 100 == 0: # if divisible by 100, check special conditions
			if year % 400 == 0:
				return True
			else:
				return False
		
		# if it is only divisible by 4
		return True
	else:
		return False

################################################################################
# Function Name: printIsLeapYear
# Parameters: year(int)
# Description: Takes year as a parameter, passes year to isLeapYear.  Prints
# if the year is a leap year to the screen
# Return: None
################################################################################
def printIsLeapYear(year):
	# print leap year status to screen
	if isLeapYear(year) == True:
		print(str(year) + " is a leap year!")
	else:
		print(str(year) + " is NOT a leap year!");

# set year as user input
year = getInput()

# print result to screen
printIsLeapYear(year)
	
	
