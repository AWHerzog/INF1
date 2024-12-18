
def encode(string, offset, salt):
    
    ints = []

    for char in string:
        ints.append(ord(char))
    
    shifted = []

    for i in ints:
        shifted.append(i + offset)
    
    res = []

    gap = len(string) - len(salt)
    realsalt = []
    realsalt.extend(salt)
    realsalt.extend(salt[:gap])

    for shift, salz in zip(shifted, realsalt):
        res.append(shift)
        res.append(salz)
    
    realres = []
    
    for word in res:
        realres.append(chr(word))
   
    return "".join(realres)
    
def decode(string, offset, salt):
    # to shifted ints
    shifted = []
    for char in string:
        shifted.append(ord(char))
    # unsalt
    unsalted = []
    for i, char in enumerate(shifted):
        if i % 2 == 1:
            continue
        unsalted.append(char)
    # un-apply offset
    ints = []
    for i in unsalted:
        ints.append(int(i - offset))
    # back to characters
    res = []
    for i in ints:
        res.append(chr(i))
    # return steps
    return shifted, unsalted, "".join(res)