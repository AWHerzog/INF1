import math

def isPowerofTwo(n):
    
    if n == 1:
        return True

    
    if n <= 0:
        return False

    
    while n % 2 == 0:
        n = n // 2

    
    return n == 1



print(isPowerofTwo(16))
print(isPowerofTwo(8))
print(isPowerofTwo(3))