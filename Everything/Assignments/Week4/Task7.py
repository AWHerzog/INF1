#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def is_prime(n):
    # implement this function
    if n == 1:
        return f"{1} is the multiplicative identity"
    
    for i in range(2, n):
        for j in range(2, n):
            if i* j == n:
                return f"{n} is not a prime number ({i} * {j} = {n})"
    
    return f"{n} is prime"

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(is_prime(36))
print(is_prime(1))
print(is_prime(37))