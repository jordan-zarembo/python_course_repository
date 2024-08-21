#08072023
#
# Challenge: Ensure that the user enters only a single character and handle cases where
# the input is not a letter.
#
# =====================================================
# Input: Ask the user to enter a single character.
# Processing: Determine whether the entered character is a vowel (a, e, i, o, u) or a consonant.
# Output: Display whether the entered character is a vowel or a consonant.
#
############################################################################################################
#
#
# My solution
#
#
l = input('   Enter a letter: ')
if l in 'aeiouAEIOU':
    print("This is a vowel.")
elif l == float('inf') or float('-inf') or l == 0:
    print("This is a number, zero, a consonant, or more than one character.")

#
# Abdul's solution to problem 9
#
#
# char_input = input('Enter a single character: ')
# #
# # processing
# #
# if len(char_input) == 1 and char_input.isalpha():
#     char = char_input.lower()
#     if char in "aeiou":
#         #output
#         print("The character is a vowel.")
#     else:
#         #output
#         print('The character is a consonant.')
# else:
#     if len(char_input) != 1:
#         #output
#         print("Error: please enter only one character.")
#     else:
#         #output
#         print("Error, the input is not a letter.")

