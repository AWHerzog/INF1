def group_by_pattern(words):
    res = {}
    for word in words:
        res[word] = len(word)

    return res


words = ["cheese", "apple", "trees", "banana", "pepper", "letter"]
print(group_by_pattern(words))
words = ["abc", "abbccc", "aaabccc", "xyz"]
print(group_by_pattern(words))