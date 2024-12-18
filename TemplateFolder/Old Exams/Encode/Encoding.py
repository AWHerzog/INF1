
def encode(string, salt, shift):
    
    s = []
    for i in string:
        s.append(i)
    
    sz = []
    for j in salt:
        sz.append(j)

    gap = len(string) - len(salt)
    saltedsalt = []
    

    saltedsalt.extend(salt)
    saltedsalt.extend(salt[:gap])
    
    JoinedChar = []
    for x, y in zip(string, saltedsalt):
        JoinedChar.append(x)
        JoinedChar.append(y)
    
    res = []
    for char in JoinedChar:
        res.append(ord(char))
    
    shifted_res = []
    
    while len(res) != len(shifted_res):
        for num in res:
            shifted_res.append(num - 2)
    
    solution = []
    
    for wrd in shifted_res:
        solution.append(chr(wrd))
    
    return JoinedChar, shifted_res, "".join(solution)

def decode(string, salt, shift):
    
    unsalted_ascii = [] #return this
    
    for char in string:
        unsalted_ascii.append(ord(char))
    
    shifted_unsalted_ascii = []

    for num in unsalted_ascii:
        shifted_unsalted_ascii.append(num + 2)

    shifted_unsalted = [] #return this

    for numr in shifted_unsalted_ascii:
        shifted_unsalted.append(chr(numr))
    
    res = []
    
    for i in shifted_unsalted:
        counter = 1 
        if counter % 2 != 0:
            res.append(i)
            counter += 1
        if counter % 2 == 0:
            shifted_unsalted.remove(i)
    
    return unsalted_ascii, shifted_unsalted, "".join(res)



print(decode("fvcwjxjvmw", "xyz", -2))