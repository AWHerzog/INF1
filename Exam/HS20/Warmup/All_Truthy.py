def all_truthy(values):
    if not values:
        return True
    
    x = [thing for thing in values if bool(thing) == True]

    return len(x) == len(values)
    


assert(all_truthy([True, "yes", "no", 1, [{}]]))
assert(all_truthy([]))
assert(not all_truthy([True, "yes", 0.0]))

