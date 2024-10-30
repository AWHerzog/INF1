
def strings_containing(strings, word):
    return [word for word in strings if word in word]


print(strings_containing(["Hello", "there", "friend"], "he" ) )
print(strings_containing(["abc", "cde", "DEF"], "de" )  )