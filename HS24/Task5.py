def count_truthy(l):
    
    res = 0
    
    for e in l:
        if bool(e) == True:
            res += 1
            count_truthy(l[1:])
        else:
            count_truthy(l[1:])
    return res


print( count_truthy([True, False, True]) )
print( count_truthy([1, 0, True, False, "hello", 0.0]) )