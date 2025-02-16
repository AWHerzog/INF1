

def square_numbers(numbers):
    '''this one just serves as an example'''
    return [ number ** 2 for number in numbers ]

def even_numbers(numbers):
    return [ number for number in numbers if number % 2 == 0]

def all_even(numbers):
    return [ round(number) if round(number) % 2 == 0 else round(number) + 1 for number in numbers  ]     

def only_integers(numbers):
    return [number for number in numbers if isinstance(number, int)]

def only_positive(numbers):
    return [abs(number) for number in numbers]

def from_1_to_1000_containing_a(a):
    return [ number for number in range (1, 1001) if str(a) in str(number)]

def multiple_of_a_and_greater_than_b(numbers, a, b):
    return [number for number in numbers if number % a == 0 and number > b]


print(only_integers([1.1, 2, 3, 4, 5, 6, -1]))
print(from_1_to_1000_containing_a(2))
print(multiple_of_a_and_greater_than_b([1.1, 2, 3, 4, 5, 6, -1], 4, 6))
