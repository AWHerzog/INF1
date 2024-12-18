def is_divisible_by(n, numbers):
    for num in numbers:
        if num == 0:  
            raise ValueError("Cannot divide by zero")
        if n % num != 0:
            return False
    return True




assert(is_divisible_by(30, [3, 6, 15]))
assert(not is_divisible_by(30, [3, 6, 29]))
try:
    is_divisible_by(30, [0, 6, 29])
    assert(False) # expected an exception!
except ValueError:
    pass # the correct exception was thrown