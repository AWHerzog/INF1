
def tally(costs, discounts, rebate_factor):
   
    res = round((sum(costs) - sum(discounts)) * rebate_factor, 2)

    if res >= 0:
        return res
    else:
        return 0
    



assert(tally([10,24], [3,4,3], 0.30)) == 7.20
assert(tally([10], [20], 0.1) == 0)