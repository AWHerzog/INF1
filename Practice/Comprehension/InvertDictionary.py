
def invert_dict(d):

    if not d:
        return {}

    res = {}

    for k, v in d.items():
        res[v] = k
    
    return res


d = {"a": 1, "b": 2, "c": 3}
print(invert_dict(d))
# Expected Output: {1: "a", 2: "b", 3: "c"}
