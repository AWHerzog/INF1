
def fizzBuzz(i):
    
    fizzbuzz_List = []
    
    for j in range(1, i + 1):
        
        if j % 3 == 0 and j % 5 == 0:
            
            fizzbuzz_List.append("FizzBuzz")
        
        elif j % 3 == 0:
            
            fizzbuzz_List.append("Fizz")
        
        elif j % 5 == 0:
            
            fizzbuzz_List.append("Buzz")
        else:
            fizzbuzz_List.append(str(j))
    
    return fizzbuzz_List
        
print(fizzBuzz(15))
