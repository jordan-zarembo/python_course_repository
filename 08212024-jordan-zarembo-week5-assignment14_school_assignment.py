#
# 08192024 Week 5 assignment 14
#
# Challenge: Handle negative exponents efficiently.
#
# ====================================
#
# Description: Develop a function named power that takes two integers, base and exponent,
# as input and returns base raised to the power of exponent.

###########################################################################################
#
#
def power (base, exponent):
    return (base ** exponent)

def power2(base, exponent):
    return pow(base, exponent)
#
def power3(base, exponent):
    if exponent < 0:
        base = 1 / base
        exponent = -exponent
    result = 1
    for _ in range(exponent):
        result *= base
        return result
#
print(power(2, 3))
print(power2(1,0))


