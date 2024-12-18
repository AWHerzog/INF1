def censor(text, censored_words):
    words = text.split()
    res = []
    for word in words:
        stripped_word = ''.join(char for char in word if char.isalpha()).lower()
        if stripped_word in censored_words:
            censored = ''.join('#' if char.isalpha() else char for char in word)
            res.append(censored)
        else:
            res.append(word)
    return " ".join(res)



print(censor("Hello, World!", ["hello"]))

assert(censor("Everything is going to be fine!", [])
    == "Everything is going to be fine!")