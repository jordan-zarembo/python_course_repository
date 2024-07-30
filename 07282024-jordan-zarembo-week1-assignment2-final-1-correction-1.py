# ## 20240723 this is the first python class work
#### 20240725 THIS IS JORDAN'S SOLUTION
####
########################################################################
####
# ## 20240725
# ## Challenge
# ## Per Abdul: "Implement error handling to ensure that the length
# ## and width entered by the user are positive numbers."
# ##
# ## Formula used for today's challenge
# ##
# ## (Length * Width)
# ##
# ######################################################################
import math
##
# ## 20240725 length module
# ##
length = input("\n\n Please enter the length of the rectangle: ")
# ##
# ## the principal amount is the "principal_integer"
length_integer = int(length)
print(f"The length is {length_integer}")
# ##
# #####################################################################
# ##
# ## 20240725 width module
# ##
width = input("\n\n Please enter the width of the rectangle: ")
# ##
# ## the rate amount is the "rate_integer"
width_integer = int(width)
print(f"The width is {width_integer}")
# ##
# ######################################################################
print('')
equation_result = (int(length) * int(width))
print(equation_result)
##
print('')
if equation_result > 0:
     print('Valid answer')
else:
     print('Syntax error')
# ##
