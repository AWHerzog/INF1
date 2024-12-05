
def stringify(n):
    
    if n % 2 == 0:
        str(n)
        return f"{n} is even"
    
    if n % 2 != 0:
        str(n)
        return f"{n} is odd"


assert stringify(10) == "10 is even"
assert stringify(5) == "5 is odd"
