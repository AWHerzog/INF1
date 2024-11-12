

import math

def checkPerfectNumber(num):
    if num < 2:
        return False
    
    divisor_sum = 1  
    limit = int(math.sqrt(num)) + 1
    
    for x in range(2, limit):
        if num % x == 0:
            divisor_sum += x
            if x != num // x:  
                divisor_sum += num // x
        if divisor_sum > num:  
            return False
    
    return divisor_sum == num

print(checkPerfectNumber(28)) 
