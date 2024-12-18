def safe_division(numerator, denominator):
    try:
        result = numerator / denominator

    except ZeroDivisionError:
        print("Division by zero is not allowed.")
    except TypeError:
        print("Inputs must be numbers.")

    else:
        print("Division successful.")
        print(f"Result: {result}")
    finally:
        print("Execution complete.")

    





safe_division(10, 2)
# Expected Output:
# Division successful.
# Result: 5.0
# Execution complete.

safe_division(10, 0)
# Expected Output:
# Division by zero is not allowed.
# Execution complete.

safe_division("10", 2)
# Expected Output:
# Inputs must be numbers.
# Execution complete.
