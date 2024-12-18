
def div_sums(numbers, divisors):
    
    res1 = []
    res2 = []
    
    x = divisors[0]
    y = divisors[-1]
    
    
    for num in numbers:
        if num % x == 0:                
            res1.append(num)
    
    for num in numbers:
        if num % y == 0:                
            res2.append(num)
    
    
    
    return list((sum(res1), sum(res2)))

            

print(div_sums([3, 1, 2, 6, 1, 9], [3, 2])) # [3+6+9, 2+6] = [18, 8]
print(div_sums([4, 4, 8], [2, 3]))
    
        



