
def process_numbers(numbers):
    return {"even": [c**2 for c in numbers if c % 2 == 0], "odd": [x**3 for x in numbers if x % 2 != 0] }


numbers = [1, 2, 3, 4, 5, 6]

result = process_numbers(numbers)
print(result)
# Expected Output:
# {
#     "even": [4, 16, 36],
#     "odd": [1, 27, 125]
# }
