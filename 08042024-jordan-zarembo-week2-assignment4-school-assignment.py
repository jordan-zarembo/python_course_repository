###########################################################################
# 08042024 Challenge
#
# Implement error handling to ensure that the user enters numeric values for the coordinates.
#
# Input: Prompt the user to enter the coordinates of two points in a 2D plane (x1, y1) and (x2, y2).
#
# Calculate the distance between the two points using the distance formula:
# sqrt((x2 - x1)^2 + (y2 - y1)^2)
#
###########################################################################

# First, calculate the coordinates.
# first, import math
import math
#
# The value for x1.
#
x1=input("     Enter your x1 coordinate:  ")
x1_value=(float(x1))
print ('')
print("     The value for x1: ", x1_value)
print('')
print('')
#
# The value for x2.
#
x2=input("     Enter your x2 coordinate:  ")
x2_value=(float(x2))
print ('')
print("     The value for x2: ", x2_value)
print('')
print('')
#
# The value for y1.
#
y1=input("     Enter your y1 coordinate:  ")
y1_value=(float(y1))
print ('')
print("     The value for y1:  ", y1_value)
print('')
print('')
#
# The value for y2.
#
y2=input("     Enter your y2 coordinate:  ")
y2_value=(float(y2))
print ('')
print("     The value for y2:  ", y2_value)
print('')
##
## The equation,
## sqrt((x2 - x1)^2 + (y2 - y1)^2)
##
print('')
print('')
z=(math.sqrt(((x2_value - x1_value)**2) + ((y2_value - y1_value)**2)))
print("The value for the equation:", z)
