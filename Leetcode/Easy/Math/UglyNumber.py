
def isUgly(n):
    
    if n <= 0:
        return False
    
    if n == 1:
        return True

    for factor in [2, 3, 5]:
        while n % factor == 0:
            n //= factor

    return n == 1
    
    
    


print(isUgly(14))