
def no_unlucky(values, unlucky):
    
    if unlucky == 0:
        return sum(values)
    
    lucky_number = 0

    for number in values:
        if number % unlucky != 0:
            lucky_number += number
    
    return lucky_number
        
print(no_unlucky([10, 24, 1], 13))
print(no_unlucky([13, 25], 13))