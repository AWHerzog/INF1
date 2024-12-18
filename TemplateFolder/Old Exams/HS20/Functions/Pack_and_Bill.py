def pack_and_bill(order, prices):
    small_boxes = 0
    large_boxes = 0
    

    sum_order = sum(order)

    while sum_order != 0:
            if sum_order >= 500:
                large_boxes += 1
                sum_order -= 500
            if 500 > sum_order > 100:
                 large_boxes += 1
                 sum_order -= sum_order
            if sum_order <= 100 and sum_order > 0:
                 sum_order = 0
                 small_boxes += 1
    
    total_price = sum(order) * 0.20 + small_boxes * 4.50 + large_boxes * 7.50
    return large_boxes, small_boxes, total_price


prices = {
    "ball":     0.20,
    "smallbox": 4.50,
    "largebox": 7.50
}
assert(pack_and_bill([1], prices)            == (0, 1, 4.70)) 
assert(pack_and_bill([500], prices)          == (1, 0, 107.50)) 
assert(pack_and_bill([600], prices)          == (1, 1, 132.00))
assert(pack_and_bill([601], prices)          == (2, 0, 135.20))
assert(pack_and_bill([50, 500, 500], prices) == (2, 1, 229.50))
