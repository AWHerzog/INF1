
def strings_containing(strings, word):
    return [char for char in strings if word.lower() in char.lower()]


print( strings_containing(["Hello", "there", "friend"], "he" ) )
print( strings_containing(["abc", "cde", "DEF"], "de" ) )