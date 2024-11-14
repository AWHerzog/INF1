
def merge_dicts(dicts, reverse_priority = False):
    result = {}

    if reverse_priority:
        for d in dicts:
            for key, value in d.items():
                if key not in result:
                    result[key] = value
    else:
        for d in reversed(dicts):
            for key, value in d.items():
                result[key] = value

    return result

d1 = {1: "a", 2: "b", 3: "c"}
d2 = {1: 1, 20: 2, 300: 3}
d3 = {1: "please", 2: "send", 300: "help"}
print(merge_dicts([d1, d2, d3]))
print(merge_dicts([d1, d2, d3], True))