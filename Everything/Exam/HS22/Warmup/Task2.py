import string

def is_perfect_pangram(sentence, alphabet = string.ascii_lowercase):
    sentence = sentence.lower()
    letters = []
    
    for c in sentence:
        if c in alphabet:
            letters.append(c)
    return len(letters) == len(set(letters)) == len(alphabet)

print(is_perfect_pangram("Mr Jock, TV quiz PhD, bags few lynx") )
print(is_perfect_pangram("a b c", "abc") )
print(is_perfect_pangram("azbzc", "abc") )
print(is_perfect_pangram("abc", "abcd") )
print(is_perfect_pangram("abb", "abc") )
