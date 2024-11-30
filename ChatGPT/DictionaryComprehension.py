
def dict_comp(data):
    
    res = {}

    for tupel in data:
        key = tupel[0]

        if key in res:
            res[key] += 1
        else:
            res[key] = 1
    
    return res


data = [('apple', 1), ('banana', 2), ('apple', 3), ('orange', 1), ('banana', 4)]

print(dict_comp(data))
