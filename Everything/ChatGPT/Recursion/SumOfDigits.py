
def sum_of_digits(n: int) -> int:
    
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)
print(sum_of_digits(123))  # Expected Output: 6
