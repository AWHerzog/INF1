def is_sub_collection(a, b):
    
    if not b:
        return True
    
    for item in b:
        if item not in a:
            return False
    return True