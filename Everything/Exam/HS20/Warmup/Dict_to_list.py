def dict_to_lists(d):
    res = []
    xes = []
    
    for key, value in d.items():
        res.append(key)
        xes.append(value)
    
    return res, xes



x = {2: "b", 1: "a"}
l1, l2 = dict_to_lists(x)
assert(sorted(l1) == [1, 2])
assert(sorted(l2) == ["a", "b"])
assert(l2[1] == x[l1[1]])