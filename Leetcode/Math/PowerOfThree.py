
import math

def isPowerOfThree(n):
    
    while n % 3 == 0:
        n /= 3

    return n == 1

print(isPowerOfThree(27))