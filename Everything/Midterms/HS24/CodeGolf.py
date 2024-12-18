
def caser(s):
    if len(s) > 5:
        return s.upper()
    
    if len(s) <= 5:
        return s.lower()



print( caser("Hello") )
print( caser("Bananas") )
print( caser("AbC") )
print( caser("i don't know!") )