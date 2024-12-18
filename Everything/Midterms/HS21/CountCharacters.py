
def count_characters(text):
    
    res = {}

    for c in text:
        if c not in text:
            res[c] = 0
        res[c] += 1

    return res