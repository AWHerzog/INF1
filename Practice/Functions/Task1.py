def square(n):
    return n * n

def apply_twice(func, x):
    res = func(x)

    return func(res)

print(apply_twice(square, 2))  # Expected Output: 16
print(apply_twice(str.upper, "hello"))  # Expected Output: 'HELLO'
print(apply_twice(lambda x: x + 3, 5))  # Expected Output: 11
