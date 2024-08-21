# 08072024
#
# Assignment 8
#
#
# Challenge: Implement error handling to ensure that the user enters valid marks (between 0 and 100)
# for each subject.
#
#
#
# =================================================
#
# Input: Ask the user to enter their marks for three subjects.
#
# Processing: Calculate the average of the marks. Determine the grade based on the average:
#
# 90 and above: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F
#
# Output: Display the calculated grade.
#
##########################################################################################################
#
print('')
print(" Enter the average of three grades:")
print('')
#
grade_1 = float(input("   Enter your first grade: "))
#
grade_2 = float(input("   Enter your second grade: "))
#
grade_3 = float(input("   Enter your third grade: "))
#
# use simple arithmetic to find average
#
avg_grade = ((grade_1 + grade_2 + grade_3) / 300)
#
# Print the average by percentile
#
print(f'   Your grade is: {avg_grade:.0%}')
#
if avg_grade >= 0.90:
    print("   You have earned an A.")
elif 0.89 >= avg_grade >= 0.80:
    print("   You have earned a B.")
elif 0.79 >= avg_grade >= 0.70:
    print("   You have earned a C.")
elif 0.69 >= avg_grade >= 0.60:
    print("   You have earned a D.")
else:
    print("   You have earned a F.")
