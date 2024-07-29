# ## 20240725
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
# import math
# ##
# ## 20240725 principal module
# ##
principal = input("\n Please enter the principal: ")
##
## the principal amount is the "principal_integer"
principal_integer = int(principal)
print(f"The value of the principal is {principal_integer}")
# ##
# #####################################################################
# ##
# ## 20240725 rate module
# ##
rate = input("\n\n Please enter the rate: ")
##
## the rate amount is the "rate_integer"
rate_integer = int(rate)
print(f"The value of the rate is {rate_integer}")
# ##
# ######################################################################
# ##
# ## 20240725 time module
# ##
time = input("\n\n Please enter the time: ")
##
## the time amount is the "time_integer"
time_integer = int(time)
print(f"The value of the time is {time_integer}")
# ##
########################################################################
# ##
# ## 20240725 creating the equation
#
print('')
equation_result = ((int(principal) * int(rate) * int(time))/100)
print (equation_result)
# ##
#
print('')
if equation_result >= 0:
     print('Valid answer')
else:
     print('Syntax error')
# ##
