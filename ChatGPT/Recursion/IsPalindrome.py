def is_palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:  
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("radar"))  # Expected Output: True
print(is_palindrome("hello"))  # Expected Output: False
