
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



nested_list = [1, [2, [3, 4], 5], [6, 7], 8]
flat_list = flatten_list(nested_list)
print(flat_list)  # [1, 2, 3, 4, 5, 6, 7, 8]


nested_list_2 = [[4.5, 6, "string"], "d", "g", ["f", 1, 6, ["another_string"]]]
flat_list_2 = flatten_list(nested_list_2)
print(flat_list_2)  # [4.5, 6, "string", "d", "g", "f", 1, 6, "another_string"]