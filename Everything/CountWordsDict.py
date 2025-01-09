
def count_letters(sentence):
    return {char: sentence.lower().count(char) for char in sentence.lower() if char.isalpha()}

# Test the function
print(count_letters("Hello World"))
# Expected: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}


