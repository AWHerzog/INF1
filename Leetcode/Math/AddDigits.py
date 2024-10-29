
def addDigits(num):
    
    x = len(str(num))

    if x == 1:
        return num
    
    
    
    while num >= 10:
        total = 0 
        for i in str(num):
             
            total += int(i)

        num = total
    
    return num

           

print(addDigits(38))






