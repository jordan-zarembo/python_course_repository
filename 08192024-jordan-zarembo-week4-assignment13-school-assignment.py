# 08272024 Week 4, Assignment 13
#
# # Challenge: Use a loop structure to compare characters from both
# # ends of the string to determine whether it is a palindrome.
# #
# #
# #
# # ===================================
# #
# # Description: Write a program that prompts the user to enter a string
# # and then checks whether it is a palindrome. A palindrome is a word, phrase,
# # number, or other sequence of characters that reads the same forward and backward.
#
########################################################################################
#
# Input
#
characters = input('   Please enter a word, number(s), or phrase: ')
#
# Processing
#
w = ""
for i in characters:
        w = i + w
#
if (characters == w):
#
# Output
#
    print("   The input is a palindrome.")
else:
#
# Output
#
    print("   Sorry, the input is not a palindrome.")
#
########################################################################################
#
# Note for Abdul:
#
# My program references the following website's model:
#
# https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/
#
# Specifically, the sub-header
#
# "Check String is Palindrome using one extra variable"
#
########################################################################################

