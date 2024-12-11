def find_both_ways(text, word):
    x = "".join(c for c in text if c not in ('!', '.', ':', '?'))
    z = x.lower()
    y = word.lower()

    if y in z:
        return (True, 1)

    if y[::-1] in z:
        return (True, -1)

    return (False, 0)

assert find_both_ways("Hello, World!", "lo, wo") == (True, 1)
assert find_both_ways("Hello, God!", "Dog") == (True, -1)
assert find_both_ways("Hello, California!", "local") == (False, 0)