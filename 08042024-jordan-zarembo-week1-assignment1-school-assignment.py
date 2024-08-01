#########################################################################
#
# ## 08012024
# ## Challenge
# ## Handle cases where the user enters non-numeric
# ## input for the principal amount, interest rate, or time period,
# ## and provide appropriate error messages.
# ##
# ##
# ## Formula used for today's challenge
# ##
# ## (Principal * Rate * Time) / 100
# ##
# ######################################################################
# ##
# ## 08012024 principal script
# ##
#
### the principal amount is the "principal_integer"
#
while True:
    try:
        principal = float(input("\n\n\n    Please enter the principal in $: "))
        xa = principal
        ya = "{:.2f}".format(xa)
        print("    The value of the principal is $", ya)
        break
    except ValueError:
        print("\n      This is not a number. Try again...")
##        print()
####
# ##
# #####################################################################
# ##
# ## 08012024 rate script
# ##
while True:
    try:
        rate = int(input("\n\n\n        Please enter the rate: "))
        print("        The value of the rate is ", rate)
        break
    except ValueError:
        print("\n   This is not a number. Try again...")
##        print()
# ##
# ######################################################################
# ##
# ## 08012024 time script
# ##
while True:
    try:
        time = int(input("\n\n\n        Please enter the time: "))
        print("\n        The value of the time is ", time)
        break
    except ValueError:
        print("\n    This is not a number. Try again...")
##        print()

# ##
########################################################################
# ##
# ## 08012024 creating the equation
#
# ((float(ya) * float(rate) * float(time))/100)
#
print('')
if ((float(ya) * float(rate) * float(time))/100) > 0:
# x = 3.14159265
#
# # Format x as a string with two decimal points
# y = "{:.2f}".format(x)
    xb = ((float(ya) * float(rate) * float(time))/100)
    yb = "{:.2f}".format(xb)
    print('Valid answer. The simple interest result is: $', yb)
elif ((float(ya) * float(rate) * float(time))/100) == 0:
     print('Syntax error. Value is zero.')
else:
    print('Syntax error. Value is less than zero.')
