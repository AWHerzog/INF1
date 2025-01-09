def is_idempotent(f, it):
    
    
    #if isinstance(it, str):
        #x = f(it)
        #return x == it.lower()
    #if isinstance(it, (float, int)):
    return (f(f(it))) == f(it)


