
def count_palindromes(sentence):
    
    out = "".join(c for c in sentence if c not in ('!','.',':', '?'))


    words = out.split()
    
    new_list = []
    for char in words:
        new_list.append(char.lower())
    
    res = 0
    for word in new_list:
        if len(word) != 1 and word == word[::-1]:
            res += 1
    
    return res


assert count_palindromes("Having fun!") == 0
assert count_palindromes("Bob and otto") == 2
assert count_palindromes("Where's Dad?") == 1
assert count_palindromes("Otto is my dad.") == 2
assert count_palindromes("I don't like pop music") == 1
