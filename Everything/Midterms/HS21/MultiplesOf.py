
def multiples_of(n, count):
    
    if not count:
        return {}
    if not isinstance(count, (int)) or count < 0:
        return False

    

    empty_dict = {}

    for x in range(1, count + 1):
        empty_dict[x] = n * x

    return empty_dict

   

print(multiples_of(3, 4))

    


    