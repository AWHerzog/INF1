
def isAnagram(s, t):
    
    if len(s) != len(t):
        return False
    
    res = list(t)
    
    for char in s:
        if char in res:
            res.remove(char)

    if res == []:
        return True
    
    return False

# Better solution according to ChatGpt
'''
def isAnagram(s, t):
    return sorted(s) == sorted(t)
'''
