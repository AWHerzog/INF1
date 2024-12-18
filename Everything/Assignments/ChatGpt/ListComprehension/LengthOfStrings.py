def get_string_lengths(strings):
    
    return [len(c) for c in strings]


strings = ["apple", "banana", "cherry", "date"]
print(get_string_lengths(strings))  # Expected output: [5, 6, 6, 4]
