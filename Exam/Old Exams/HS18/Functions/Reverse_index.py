

def rev_idx(words):
    
    d = {}

    idx = 0

    for c in words:
        c = c.lower()

        if not c in d.keys():
            d[c] = []
        d[c].append(idx)
        idx += 1
    return d

    
print(rev_idx([]))
print(rev_idx(["a","b"]))
print(rev_idx(["a","B","A","aa"]))