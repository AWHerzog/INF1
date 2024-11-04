
def length(iterable):
    if iterable in ["", [], ()]:
        return 0
    return 1 + length(iterable[1:])

# examples
print( length([1, 2, [3, 4]]) )
print( length(("a", 1, 2, None)) )
print( length("oh dear") )