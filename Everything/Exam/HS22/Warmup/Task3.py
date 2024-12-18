
def padded_dict(keys, values, padding=None):
    
    d = {}
    for i in range(len(keys)):
        try:
            val = values[i]
        except IndexError:
            val = padding
        d[keys[i]] = val
    return d
    

print(padded_dict([1, "b", 3], [55, 66, 77] ) )
print(padded_dict([1, "b", 3], [55] ) )
print(padded_dict([1, "b"], [55, 66, 77] ) )