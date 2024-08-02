###############################################################
# 08042024
#
# Input: Prompt the user to enter a time duration in hours.
# Processing: Convert the time duration to minutes and seconds.
# Output: Display the converted time duration in minutes and seconds.
#
##############################################################
#
#
hour=input("     Please enter the hour value: ")
hour_value=(int(hour))
print('')
print('')
#
y=(hour_value * 60)
print("     The value for minutes:", y)
print('')
#
z=(hour_value * 3600)
print('')
print("     The value for seconds:", z)
print('')
