def categorize_characters(string):
    return {
          "letters": [char for char in string if char.isalpha()],
          "digits": [num for num in string if num.isdigit()],
          "others": [char for char in string if not char.isalnum()]  
            
            
    }

# Example usage:
print(categorize_characters("Hello123! How's it going?"))
# Expected Output:
# {
#     "letters": ['H', 'e', 'l', 'l', 'o', 'H', 'o', 'w', 's', 'i', 't', 'g', 'o', 'i', 'n', 'g'],
#     "digits": ['1', '2', '3'],
#     "others": ['!', ' ', "'", '?']
# }
