
def prod(x,y):
    if x == 1:
        return y
        
    return y + prod(x - 1, y)


(prod(2, 0) == 0)
print(prod(5, 2))