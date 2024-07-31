####################################################################
# ## 20240804 Assignmwnt 3
# ## Challenge
# Challenge: Provide feedback to the user based on their BMI category
# (e.g., underweight, normal weight, overweight, obese).
#
# Input: Prompt the user to enter their weight in kilograms and height in meters.
# Processing: Calculate the BMI using the formula: BMI = Weight / (Height^2).
# Output: Display the calculated BMI.
#
##
## NOTE TO ABDUL:
##
## I had the user enter weight in pounds
## The weight in kilograms is displayed
##
## and enter the height in feet and inches
## the height in meters is displayed
##
## the calculation is done in kg/m^2
##
## I did this because I don't know my weight in kilograms and height in meters.
##
########################################################################
#
# 20240804 weight conversion
#
# conversion of lbs to kg
# x * 0.454
#
lbs = input("   Enter your weight in pounds: ")
weight_in_lbs=int(lbs)
weight_in_kg=(int(lbs) * 0.454)
print ('')
print(("Your weight in kilograms is: "), weight_in_kg)
print('')
#
###########################################################################
#
# 20240729 conversion of feet and inches to meters
#
#
feet = input("   Enter your height in feet: ")
height_in_feet=int(feet)
inches = input("   Enter your height in inches: ")
height_in_inches=int(inches)
#
# the conversion equation for feet/inches to meters is
# d(m) = d(ft) × 0.3048 + d(in) × 0.0254
#
height_in_meters=float((int(feet) * 0.3048) + (int(inches) * 0.0254))
print ('')
print(("Your height in meters is:"), height_in_meters)
#
##########################################################################
#
# 20240709 bmi calculation
#
# remember: equation for bmi is kg/m^2
#
# 07292024 the following code until the end of the programming
# is taken from this website:
# https://www.datainsightonline.com/post/simple-bmi-calculator-using-python
#
bmi=(int(weight_in_kg)) / (int(height_in_meters ** 2))
print('')
print("Your BMI is: ", bmi)
print('')
print('')
##
# Per the CDC:
#
# Underweight <= 18.5
# Healthy Weight 18.5 < 25
# Overweight 25 < 30
# Obesity <30
#
##
if bmi <= 18.5:
    print("You are underweight.")
elif 18.5 <= bmi <= 24.9:
    print("Your weight is healthy.")
elif 25.0 <= bmi <= 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
##


