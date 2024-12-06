
def calc(expression):
    
    list1 = expression.split()
    
    x = float(list1[1])
    y = float(list1[2])

    if list1[0] == "+":
        return x + y
    if list1[0] == "-":
        return x - y
    if list1[0] == "/":
        if y == 0:
            raise ValueError
        return x / y
    if list1[0] == "*":
        return x * y


assert calc("+ 1 2") == 3
assert calc("- 1 2") == -1
assert calc("* 1 2") == 2
assert calc("/ 1 2") == 0.5
assert calc("* 1 -2") == -2
assert calc("* 10.5 2") == 21
assert calc("* -10.5 -2") == 21