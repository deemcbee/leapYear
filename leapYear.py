def isLeapYear (year):
	#function for calculating if this is a leap year
	if (year-1800) % 4 == 0:
		print("This is a leap year")
	else:
		print("This is not a leap year")

testYear = int(input("Please enter a year after 1800: "))

isLeapYear(testYear)

