
def merge_dicts(dicts, reverse_priority=False):
    res = {}

    if reverse_priority:
        dicts = reversed(dicts)
        
    for dictionary in dicts:
        for k, v in dictionary.items():
            res[k] = v
    
    return res



d1 = {1: "a", 2: "b", 3: "c"}
d2 = {1: 1, 20: 2, 300: 3}
d3 = {1: "please", 2: "send", 300: "help"}

print(merge_dicts([d1, d2, d3]))
# Expected Output: {1: 'please', 2: 'send', 3: 'c', 20: 2, 300: 'help'}

print(merge_dicts([d1, d2, d3], reverse_priority=True))
# Expected Output: {1: 'a', 2: 'b', 3: 'c', 20: 2, 300: 3}