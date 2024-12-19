
def transform(numbers):
    
    return [num * 2 if num > 99 else num for num in numbers if num % 2 == 0 and num > len(numbers)] 


print(transform([2, 103, 10, 5, 10, 104, 2222, 20]))
print(transform([1, 2, 3, 4, 5]))
print(transform([2, 3, 4, 5, 6]))
print(transform([1000]))