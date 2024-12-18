def powerset(nums):
    nums = list(set(nums))

    if not nums:
        return [[]]
    
    rest = powerset(nums[1:])

    return rest + [[nums[0]] + subset for subset in rest]

test_input = {1, 2, 3}
result = powerset(test_input)
print(result)


# The following lines call the function and print the return
# value to the Console. This way you can check what they do.
test_set = {1, 2, 3}
result = powerset(test_set)
# Example output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
# Note that the order of the powerset could differ depending on the implementation.
# Make sure to look at the predefined test and adjust it if so.
print(result)