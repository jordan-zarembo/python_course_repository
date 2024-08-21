# # 08192024 Week 4, Assignment 12
#
# Challenge: Use nested loop structures to print the pattern efficiently and neatly.
# Allow the user to specify the character used for the pattern.
#
#
#
# =========================================
#
# Description: Develop a program that prompts the user to enter the number of rows for a pattern
# and then prints a pattern of asterisks (*) in the form of a right triangle.
#
##################################################################################################
#
# Input
#
# The "right angle input" allows the user to specify the integer size of the character pyramid.
#
right_triangle = (int(input("   Please specify the integer number of rows in a right angle character triangle: ")))
#
# Here the number variable is controlled by the user input and is not a static number.
#
print('')
character = input("   What character(s) would you like to use? ")
print('')
#
# Multiple different characters can be used, like "$qA" or something.
#
# Processing
#
# beginning of nested for loop for the program:
#
# use of the range function
#
for row in range (right_triangle):
#
# The range is determined by the user's integer input.
#
# using range to determine the number of columns
#
    for col in range(row + 1):
#
# Here the range is used with (row + 1) to include another row of characters, and so on
#
#
# Output
#
        print(character, end='')
#
# The end='' prints a new line, and does not print the characters in a straight vertical line.
#
# Output
#
    print()
#
# A print statement closes the pyramid after the specified number of rows are done.
#
#
#################################################################################################
#
# Note for Abdul:
#
# I referenced the following websites for information on how to create a right angle symbol triangle.
#
# https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/
#
# https://www.geeksforgeeks.org/python-print-inverted-star-pattern/
#
# https://www.tutorialgateway.org/python-program-to-print-right-angled-triangle-star-pattern/
#
# From prepinsta.com: https://tinyurl.com/4yvfpbb7
#
# And in particular, https://stackoverflow.com/questions/25921016/using-python-to-create-a-right-triangle
#
# Thanks,
# Jordan
#
