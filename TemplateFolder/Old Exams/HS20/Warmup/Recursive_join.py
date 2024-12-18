
def recursive_join(delim, values):
    if not values:
        return ""
    
    if len(values) == 1:
        return values[0]

    return values[0] + delim + recursive_join(delim, values[1:])


assert(recursive_join(" ", ["Hello", "world"]) == "Hello world")
assert(recursive_join(" <o> ", ["a", "b", "c"]) == "a <o> b <o> c")
assert(recursive_join("", ["a", "b", "c"]) == "abc")
assert("Your solution must be recursive!")