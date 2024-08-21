#########################################################################
#
#
#08042023
#
# Challenge: Handle cases where the user enters non-numeric input for the year and provide appropriate
# error messages.
#
# ----------------------------------------------------------------------------------------------------------
#
# Input: Prompt the user to enter a year.
#
# Processing: Determine whether the entered year is a leap year or not.
# A leap year is divisible by 4 but not by 100 unless it is also divisible by 400.
#
# Output: Display whether the entered year is a leap year or not.
#
#
# NOTE TO ABDUL:
#
# The expression ((year % 4 == 0 and year % 100 !=0) or (year % 400 == 0))
# Has been taken from:
# https://www.upgrad.com/tutorials/software-engineering/python-tutorial/leap-year-program-in-python/
# I am not the original author of this expression.
# Thanks,
# Jordan
#
#
#
#########################################################################
#
#
# Input
#
#
year = (int(input("   Please enter a year: ")))
#
# Processing
#
if bool("0") == ((year % 4 == 0 and year % 100 !=0) or (year % 400 == 0)):
    print("   This is a leap year.")
#
if bool("1") != ((year % 4 == 0 and year % 100 !=0) or (year % 400 == 0)):
        print("   This is not a leap year.")
#
# Output
#
