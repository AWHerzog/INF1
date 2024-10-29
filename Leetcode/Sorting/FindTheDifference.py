
def findTheDifference(s, t):
    
    if not s:
        return t
    
    
    
    char_list1 = []
    char_list2 = []

    
    for x in s:
        char_list1.append(x)

    for y in t:
        char_list2.append(y)
    
        



print(findTheDifference(("abcd"), ("abcde")))