
def is_isogram(sentence):

    if not isinstance(sentence, str):
        raise TypeError
    tout = "".join(c for c in sentence if c not in ('!','.',':', '?', '-'))
    out = "".join(c.lower() for c in tout if c.isalpha())

    seen = set()

    for char in out:
        if char in seen:
            return False
        seen.add(char)
    return True

    


assert is_isogram("uncopyrightable")
assert is_isogram("The big dwarf only jumps.")
assert is_isogram("Apple-ale")
assert (not is_isogram("bass"))
assert (not is_isogram("Tart"))
