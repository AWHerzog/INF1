def sort_dict_values(d):
    res = {}
    for key, value in d.items():
        res[key] = sorted(value)
    return res

# examples
print( sort_dict_values({"a": [3, 1, 2]}) )
print( sort_dict_values({1: ["z", "az"], 2: [1]}) )