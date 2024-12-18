def merge_dicts(dicts, reverse_priority=False):
    res = {}
    if reverse_priority:
        dicts = reversed(dicts)
    for d in dicts:
        for k, v in d.items():
            res[k] = v
    return res