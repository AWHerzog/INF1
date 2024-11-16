

def encode(string, salt, offset):
    # add salt
    salted = []
    salt_index = 0
    for char in string:
        salted.append(char)
        salted.append(salt[salt_index])
        salt_index += 1
        if salt_index == len(salt):
            salt_index = 0
    # convert to ints
    ints = []
    for char in salted:
        ints.append(ord(char))
    # apply offset
    shifted = []
    for i in ints:
        shifted.append(i + offset)
    # back to string
    res = ""
    for i in shifted:
        res += chr(i)
    # return steps
    return salted, shifted, res

def decode(string, salt, offset):
    # to shifted ints
    shifted = []
    for char in string:
        shifted.append(ord(char))
    # un-apply offset
    ints = []
    for i in shifted:
        ints.append(i - offset)
    # back to characters
    salted = []
    for i in ints:
        salted.append(chr(i))
    # unsalt
    res = ""
    for i, char in enumerate(salted):
        if i % 2 == 1:
            continue
        res += char
    # return steps
    return shifted, salted, res