
def powerset(nums):
    nums = list(set(nums))

    if not nums:
        return [[]]
    
    rest = powerset(nums[1:])

    return rest + [[nums[0]] + subset for subset in rest]

test_input = {1, 2, 3}
result = powerset(test_input)
print(result)

    



