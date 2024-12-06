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
    


print(count_palindromes("Having fun!"))
print(count_palindromes("Bob and otto")) 
print(count_palindromes("Where's Dad?"))
print(count_palindromes("Otto is my dad."))
print(count_palindromes("I don't like pop music"))