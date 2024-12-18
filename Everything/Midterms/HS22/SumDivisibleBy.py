
def sum_divisibles(limit, divisor):

    res = 0
    
    for x in range(1, limit):

        if x % divisor == 0:
            res += x
    
    return res


print( sum_divisibles(5, 2) )
print( sum_divisibles(11, 5) )