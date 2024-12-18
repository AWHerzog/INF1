def invert(d):
    
    if not d:
        return {}
    
    inverted_dict = {}
    
    for key, value in d.items():
        if value in inverted_dict:
            inverted_dict[value].append(key)
        else:
            inverted_dict[value] = [key]

    for key in inverted_dict:
        inverted_dict[key] = sorted(inverted_dict[key])

    return inverted_dict


print(invert({"a":1, "b":1, "c":3}))