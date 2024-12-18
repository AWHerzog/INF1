def count_letters(s):
    
    count_upper = sum(1 for ltr in s if ltr.isupper())
    count_lower = sum(1 for ltr in s if ltr.islower())
    return {"upper": count_upper, "lower": count_lower}


d = count_letters("Abc Defg HiJ!")
assert d["upper"] == 4 and d["lower"] == 6


