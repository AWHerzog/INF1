def classify_numbers(numbers):
    result = {num: ("even" if num % 2 == 0 else "odd") for num in numbers}
    
    return result

numbers = [1, 2, 3, 4, 5]
print(classify_numbers(numbers))
