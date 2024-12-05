def filter_words_by_length(words, n):
    return [c for c in words if len(c) >= n]

words = ["apple", "banana", "kiwi", "pineapple", "grape"]
n = 5
print(filter_words_by_length(words, n))  