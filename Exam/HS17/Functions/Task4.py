
def mirror(s):

    if not s:
        return s
    
    if len(s) == 1:
        return s

    res = []
    res.extend(s)
    
    reverse = s[::-1]
    res.extend(reverse[1:])

    string = "".join(res)
    
    return string


assert mirror("") == ""
assert mirror("a") == "a"
assert mirror("abc") == "abcba"