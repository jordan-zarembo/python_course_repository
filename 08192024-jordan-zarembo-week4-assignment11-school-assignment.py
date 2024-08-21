# 08192024 Week 4, Assignment 11
#
#
# Challenge: Use a loop structure to generate the Collatz sequence until it reaches 1.
# Handle cases where the user enters a non-numeric input.
#
# =================================
# Description: Write a program that generates the Collatz sequence for a given positive integer
# entered by the user. The Collatz sequence is generated iteratively by repeatedly applying
# the following rules:
#
# If the current number is even, divide it by 2.
# If the current number is odd, multiply it by 3 and add 1.
#
# Modulo is used here to check for remainders. If there is no remainder, then the Collatz sequence is regular.
#
# Help and suggestions have been taken from the following Stack websites:
#
# https://stackoverflow.com/questions/11233355/generating-a-list-of-even-numbers-in-python
# https://www.geeksforgeeks.org/program-to-print-collatz-sequence/
#
#################################################################
#
#
# What is the collatz sequence: either if even, x / 2 or if odd, 3x + 1
#
user_input = input('   Enter a positive integer: ')
#
while True:
    if user_input.isdigit():
        number = int(user_input)
        if number > 0:
            break
        else:
            user_input = (input("must be a positive integer. Enter again: "))
    else:
        user_input = input("Invalid input. Please enter a positive integer: ")
#
# Enter the sequence
print("Collatz Sequence: ")
#
while number != 1:
    print(number, end=" -> ")
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * +number + 1
print(1)























