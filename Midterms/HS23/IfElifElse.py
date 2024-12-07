
def discounted_price(original, low, normal_discount, high, high_discount):
    if original < low:
        return round(original)
    elif  high > original >= low:
        return round(original * normal_discount)
    
    return round(original * high_discount)
    


print(discounted_price(100, 200, 0.9, 500, 0.7))
print(discounted_price(300, 200, 0.9, 500, 0.7))
print(discounted_price(888, 200, 0.9, 500, 0.7))