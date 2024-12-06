def intersperse(s, l):
    result = []
    n = len(l)
    
    for i, char in enumerate(s):
        result.append(char)
        if i < len(s) - 1:  
            result.append(l[i % n])
    
    return ''.join(result)

