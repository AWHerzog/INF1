def normalize(number, lower, upper):
    return min(upper, max(lower, number))

print( normalize(1.5, 0, 1) )
print( normalize(15, 10, 20) )