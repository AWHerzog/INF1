def is_valid_encoding(a, b, mapping):
    

    if a == b and (a == None or a == ''):
        return True
    
    elif (a == None and b == '') or (a == '' and b == None):
        return False
    
    else:
        tmp = ''.join([mapping.get(i, i) for i in a])
        return tmp == b