
def check(speed, limit):
    
    if limit == 0:
        return True
    
    if speed > limit:
        return False
    
    return True