
def reversed_padded_dict(keys, values, padding=None):
    res = {}

    for i, value in enumerate(values):
        if i < len(keys):
            res[value] = keys[i]
        else:
            res[value] = padding  
    return res




print(reversed_padded_dict([1, "b", 3], [55, 66, 77]))  
# Output: {55: 1, 66: "b", 77: 3}

print(reversed_padded_dict([1, "b", 3], [55]))  
# Output: {55: 1, None: "b", None: 3}

print(reversed_padded_dict([1, "b"], [55, 66, 77]))  
# Output: {55: 1, 66: "b"}