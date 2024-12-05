
def hailstone(n):
    
    res = [n]
    el = n
    while el != 1:
        
        if el % 2 == 0:
            el = el / 2
        else:
            el = el * 3 + 1
        res.append(el)
    return res

assert hailstone(1) == [1]
assert hailstone(3) == [3, 10, 5, 16, 8, 4, 2, 1]
assert hailstone(7) == [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]