
#numbers = key
#value = potential_divisors
def divisor_finder(numbers, potential_divisors):
    return {x: y for x in numbers for y in potential_divisors if x % y == 0}




print(divisor_finder([12], [2, 3, 4, 5]))
