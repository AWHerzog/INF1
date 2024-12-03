def same_result(f, g, it):
    return f(it) == g(it)



print( same_result(len, sum, [1, 1]) )
print( same_result(str.title, str.upper, "world") )
print( same_result(bool, str.isdigit, "1") )