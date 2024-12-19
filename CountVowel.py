def count_vowels(sentence): 
    res = {vowel: 0 for vowel in "aeiou"}  # Initialize with all vowels set to 0
    
    x = [c.lower() for c in sentence if c.isalpha()]
    
    for char in x:
        if char in res:  # Check if char is a vowel
            res[char] += 1
            
    return res

# Example usage:
print(count_vowels("Hello World"))  
# Expected: {'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0}

print(count_vowels("Python is fun!"))  
# Expected: {'a': 0, 'e': 0, 'i': 1, 'o': 1, 'u': 1}

print(count_vowels(""))  
# Expected: {'a': 0, 'e': 0, 'i': 0, 'o': 0}

