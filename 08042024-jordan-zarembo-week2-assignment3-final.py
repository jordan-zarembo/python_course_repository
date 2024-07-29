# ## 20240804 Assignmwnt 3
# ## Challenge
# Challenge: Provide feedback to the user based on their BMI category
# (e.g., underweight, normal weight, overweight, obese).
#
# Input: Prompt the user to enter their weight in kilograms and height in meters.
# Processing: Calculate the BMI using the formula: BMI = Weight / (Height^2).
# Output: Display the calculated BMI.
#
# BMI categories (per CDC):
#
# Underweight <18.5 kg/m^3
# Healthy Weight 18.6 < a < 24.9 kg/m^2
# Overweight 25 < b < 29.9 kg/m^3
# Class 1 Obesity 30 < c < 34.9 kg/m^2
# Class 2 Obesity 35 < d < 39.9 kg/m^2
# Class 3 Obesity e > 40 kg/m^2
#
########################################################################
#
# 20240804 weight conversion
#
# conversion of lbs to kg
# x * 0.454
#
lbs = input("   Enter your weight in pounds: ")
weight_in_lbs=float(lbs)
weight_in_kg=(float(lbs) * 0.454)
print ('')
print(f"Your weight is {weight_in_kg} kilograms")
print('')
#
#########################################################################
#
# 20240729 conversion of feet and inches to meters
#
#
feet = input("   Enter your height in feet: ")
height_in_feet=int(feet)
inches = input("   Enter your height in feet: ")
height_in_inches=int(inches)
#
# the conversion equation for feet/inches to meters is
# d(m) = d(ft) × 0.3048 + d(in) × 0.0254
#
height_in_meters=float((int(feet) * 0.3048) + (int(inches) * 0.0254))
print ('')
print(f"Your height in meters is {height_in_meters}")
#
##########################################################################
#
# 20240709 bmi calculation
#
# remember: equation for bmi is kg/m^2
#
# 07292024 the following code is taken from this website
# https://www.datainsightonline.com/post/simple-bmi-calculator-using-python
#
def bodymassindex(weight_in_kg, height_in_meters):
    return round((weight_in_kg / height_in_meters**2),2)
#
bmi = bodymassindex(weight_in_kg, height_in_meters)
print('')
print("Your BMI is: ", bmi)
#
