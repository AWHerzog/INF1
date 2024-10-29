
def findTheDifference(s, t):
    
    if not s:
        return t
    
    
    
    char_list1 = list(s)
    
    
    for char in t:
        if char in char_list1:
            char_list1.remove(char)

        else:
            return char


    
        



print(findTheDifference(("abcd"), ("abcde")))