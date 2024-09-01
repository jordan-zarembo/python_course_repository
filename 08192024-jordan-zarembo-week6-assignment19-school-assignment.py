# 08202024 Assignment 19
#
#
# Challenge: Implement the sorting algorithm without using any built-in sorting functions.
#
# ====================================
# Description: Develop a function called sort_list that takes a list of numbers as input
# and returns a new list containing the same elements sorted in ascending order.
#
############################################################################################
#
#
#
def sort_list(list1):
    primes = list(set(list1))
    return primes

lista = [2,5,7,9,17,11]

result = sort_list(lista)
print("These are the primes in ascending order:", result)








