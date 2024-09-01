# 08202024 Assignment 15
#
# Challenge: Write the function using recursion.
#
# ===================================
# Description: Create a function named is_palindrome that takes a string as input and
# returns True if it is a palindrome, and False otherwise.
######################################################################################
#' (Beginning of quotation mark)
#
def is_palindrome(s):
    s = s.lower()
    l = len(s)
#
    if l < 2:
        return True
#
    elif s[0] == s[l - 1]:
        return is_palindrome(s[1: l - 1])
#
    else:
        return False
#
#
s = input("   Please select a word, number(s), or phrase to see if it's a palindrome: ")
#
answer = is_palindrome(s) # see notation below [1]
#
# [1] At line 25 the variable "s" from the function is defined with an input. The function is called
# at line 27 and given the variable "answer".
#
if answer: # see notation below [2]
    print("True, it is a palindrome")
#
else:
    print("False, it is not a palindrome")
#
# [2] An if-else statement controls the output of the variable answer. If the output of lines 11 - 22
# (the function) matches the input "answer" and is True (line 32), line 36 (the True statement) is printed.
# If not, the else takes care of all other False entries.
#
# " (end of quotation mark) [3]
#######################################################################################
#
# Note to Abdul:
#
# [3] This code was sourced from
# https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/
# Scroll down to "Check String is Palindrome using recursion"
#
# my annotations in hashtags
