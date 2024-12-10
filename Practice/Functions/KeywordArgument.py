def process_numbers(*args, operation, round_result=False):
    if operation not in {"sum", "product", "average"}:
        raise ValueError("Invalid operation. Must be 'sum', 'product', or 'average'.")

    if operation == "sum":
        result = sum(args)
    elif operation == "product":
        result = 1
        for val in args:
            result *= val
    elif operation == "average":
        result = sum(args) / len(args)

    return round(result, 2) if round_result else result


                




print(process_numbers(1, 2, 3, operation="sum"))           # Expected Output: 6
print(process_numbers(1, 2, 3, operation="product"))       # Expected Output: 6
print(process_numbers(1, 2, 3, operation="average"))       # Expected Output: 2.0
print(process_numbers(1, 2, 3, operation="average", round_result=True))  # Expected Output: 2.00
