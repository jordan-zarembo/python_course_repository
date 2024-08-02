########################################################################
####
# ## 07252024
# ## Challenge
# ## Per Abdul: "Implement error handling to ensure that the length
# ## and width entered by the user are positive numbers."
# ##
# ## Formula used for today's challenge
# ##
# ## (Length * Width)
# ##
# ######################################################################
# ## 20240725 length script
# ##
# length = (int(input("\n\n      Please enter a length: ")))
#
#
length = (input("\n\n      Please enter a length: "))

# #####################################################################
# ##
# ## 20240725 width script
#
width = (input("\n\n      Please enter a width: "))
#
#######################################################################
print('')
equation = (float(length) * float(width))
##
print('')
if equation > 0:
     print('Valid answer. The positive value equation result is:', equation)
else:
     print('Syntax error. The equation result is: ', equation)
     print('Values must be positive.')
     print('Please run the program again.')
# ##
