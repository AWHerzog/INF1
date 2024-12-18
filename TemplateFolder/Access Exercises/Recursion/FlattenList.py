def flatten_list(nested_list):
    if not isinstance(nested_list, list):
        raise TypeError("Expected argument has to be a list.")
    
    if not nested_list:
        return []
    
    res = []

    for element in nested_list:
        if isinstance(element, list):
            res.extend(flatten_list(element))
        else:
            res.append(element)

    return res
