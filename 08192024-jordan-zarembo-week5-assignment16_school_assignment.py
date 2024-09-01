# Assignment 16
# Challenge: Optimize the function to handle large input numbers efficiently.
#
# =====================================================
# Description: Develop a function called is_prime that takes a positive integer as input and returns True 
# if it is a prime number, and False otherwise.
#
#############################################################################################
#
# for this section refer to https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
# scroll down to "Check Prime Numbers Using Recursion"
# also
# check https://www.geeksforgeeks.org/how-to-fix-recursionerror-in-python/
# scroll down to "Increase recursion limit"
#
import math
#
def is_prime(number, itr):
#
    if itr == 1 or itr == 2:
        return True
#
    if number % itr == 0:
        return False
#
    if is_prime(number, itr - 1):
        return False
#
    if is_prime(number, itr):
        return True
#
#
# for this section refer to https://blog.stackademic.com/calculating-prime-factors-in-python-4ade6f1161f5
# alap
# check https://code.sololearn.com/c20HpGq6yw2Q/?ref=app
# also
# check https://blog.stackademic.com/calculating-prime-factors-in-python-4ade6f1161f5
#
def prime_factors(n):
    factors = []
#
    while n >= 2 and n % 2 == 0:
        factors.append(2)
        n //= 2
#
    i = 3
    while i + i <= n:
        while n % i == O:
            factors.append(i)
            n //= i
        i += 2
#
if n > 1:
    factors.append(n)
#
#
# check here ScholarHat: https://tinyurl.com/55yvkzb9
#
if num == (int(input("     Please enter a number to tell if it's prime or not: "))):
#
    itr = int(pow(num, 0.5) + 1)
#
else:
#
    print(is_prime(num, itr))
#


