
def count(l):
    
    res = 0
    for e in l:
        if isinstance(e, list):
            res += count(e)
        else:
            res += 1
    return res

print(count([]))
print(count([[],[]]))
print(count([1, "", [{}], [[True], 4]]))