def filter_odd_numbers(numbers):
    return [n for n in numbers if n % 2 != 0]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_odd_numbers(numbers))  
