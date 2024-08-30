import math
from functools import reduce
def gcd(a, b):
    return math.gcd(a, b)
def lcm(a, b):
    return abs(a * b) 
def gcd_n_numbers(numbers):
    return reduce(gcd, numbers)
def lcm_n_numbers(numbers):
    return reduce(lcm, numbers)
numbers = [16, 20]
gcd_result = gcd_n_numbers(numbers)
lcm_result = lcm_n_numbers(numbers)

print(f"GCD = {gcd_result}")
print(f"LCM = {lcm_result}")
