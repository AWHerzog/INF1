import random

def lottery(values):
    draw = random.sample(range(1,51), k=len(values))
    res = []
    
    
    for num in draw:
        if num in values:
            res.append(num)
    
    return draw, len(res)





guess = [1,2,3,4,5]
res = lottery(guess)
assert(len(res[0]) == len(guess))
assert(res[1] in range(0,len(guess)+1))


