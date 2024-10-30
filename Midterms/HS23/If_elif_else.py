
def discounted_price(original: int, low: int, normal_discount: int, high: int, high_discount: int ):
    
    if original < low:
        return round(original)
    if high > original >= low:
        return round(original * normal_discount)
    if original >= high:
        return round(original * high_discount)



print(discounted_price(100, 200, 0.9, 500, 0.7))
print(discounted_price(300, 200, 0.9, 500, 0.7))
print(discounted_price(888, 200, 0.9, 500, 0.7))

#100
#270
#622