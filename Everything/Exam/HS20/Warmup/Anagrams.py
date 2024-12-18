def are_anagrams(a, b):
    texta = "".join(c.lower() for c in a if c.isalnum())
    textb = "".join(c.lower() for c in b if c.isalnum())

    return sorted(texta) == sorted(textb)

   
assert(are_anagrams("The Meaning of Life.", "The fine game of nil!"))
assert(not are_anagrams("The Meaning of Life", "Work"))
    