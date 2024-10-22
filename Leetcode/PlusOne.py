

def plusOne(digits):

    for i in range(len(digits)-1, -1, -1):
    
        if digits[i] < 9:
             digits[i] += 1

             return digits
        
        if digits[i] == 9: 
            digits[i] = 0
            return digits
    
    

print(plusOne([1, 0, 9]))
             
        
       
        






        


