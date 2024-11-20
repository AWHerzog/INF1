import string

def is_palindrome(s):

    s = s.strip()
    s = s.lower()
    s = s.translate(str.maketrans('', '',string.punctuation))
                     

    if len(s) == 0:
        return True
    
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    
    return False





# The following lines call the function and prints the return
# value to the Console. This way you can check what it does.
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("No lemon, no melon"))
print(is_palindrome("This is not a palindrome"))