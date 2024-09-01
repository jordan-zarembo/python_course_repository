# Final Project
#
# Begun 08042024
#
#############################################################################################################
#
# September 1 2024
#
# Hi Abdul! My final project work is in large part a modification of some of your class solutions.
# I'm using your programs as a reference. There is some copying and modification of your program code.
# Just wanted to give you due credit for your work. Thanks for teaching the course!
#
# I have used Google AI for information, but I have not copied code from AI into the code for the assignment.
# AI code is usually not applicable to what I need to complete the assignment.
#
#############################################################################################################
#
#
# For below [1], please reference
# https://stackoverflow.com/questions/66833367/user-input-from-defined-list-in-python
#
# The following code will allow a user to select their name
#
names = ["Tommy", "Cam", "Susie", "Jane"]
user = input("   Please enter a name: ")
if user in names:
    print("Authorized user.")
else:
    print("invalid user")
#
# For below [2], please reference
# https://stackoverflow.com/questions/66409689/compare-user-input-with-a-list-in-python
# also reference
# https://www.geeksforgeeks.org/python-match-case-statement/
#
def match_name_fruits(dictionary, name):
#
    match dictionary:
        case {"name": n, "fruit": f}:
            print(f"Name:{n}, Fruit:{f}")
        case {"name": n, "fruit": f}:
            print(f"Name:{n}, Fruit:{f}")
        case {"name": n, "fruit": f}:
            print(f"Name:{n}, Fruit:{f}")
        case _ :
            print("Data does not exist")
#
    if name == Tommy:
        match_name_fruits({"name": "Tommy", "fruit":  "kumquat"})
    elif name == Cam:
        match_name_fruits({"name": "Cam", "fruit":  "apple"})
    elif name == Susie:
        match_name_fruits({"name": "Susie", "fruit":  "dragonfruit"})
    elif name == Jane:
        match_name_fruits({"name": "Jane", "fruit":  "kiwi"})
    else:
        print("Sorry, no match")
