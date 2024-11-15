
def padded_dict(keys, values, padding=None):
    res = {}

    for i, key in enumerate(keys):
        if i < len(values):  
            res[key] = values[i]
        else:  
            res[key] = padding

    return res

print( padded_dict([1, "b", 3], [55, 66, 77] ) )
print( padded_dict([1, "b", 3], [55] ) )
print( padded_dict([1, "b"], [55, 66, 77] ) )