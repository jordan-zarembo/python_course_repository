##################################################################################################
#
# 08052024
#
#
# Challenge: Implement error handling to ensure that the user enters a positive integer for the age.
#
# ==================================
# Input: Prompt the user to enter their age.
# Processing: Classify the age into different categories:
# Under 18: Minor
# 18-65: Adult
# Above 65: Senior citizen
# Output: Display the category based on the entered age.
#
##################################################################################################
#
# Defining the age
# Code taken from Dave Gray repository:
# https://github.com/gitdagray/python-course/blob/main/lesson05/rps.py
# #
# import sys
# #
# age = int(input("     Enter an age: "))
# #
# age_value = int(age)
# #
# if age_value <= 0:
#     sys.exit("You must enter a positive integer for the age value.")
# #
# ###################################################################################################
# #
# # 08052024 the following code until the end of the programming
# # is modified from this website:
# #
# #
# if (age < 18):
#     print("     You are a minor.")
# elif (18 <= age <= 65):
#     print("     You are an adult.")
# else:
#     print("     You are a senior citizen.")
#
######################################################################################################
#
age_input = input('enter your age:')
#
if age_input.isdigit():
    age = int(age_input)
    if age > 0:
        if age < 18:
            print('Minor')
        elif 18 == 65:
            print('Adult')
        else:
            print('senior citizen')
else:
    print("Error: Age must be a positive number")
    print("Error: Invalid input. Please enter a positive number.")
