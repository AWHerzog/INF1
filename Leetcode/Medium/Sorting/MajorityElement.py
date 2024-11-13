import math

def majorityElement(nums):
    
    length = math.floor(len(nums) / 3)

    new_nums = []
    
    for i in nums:
        if nums.count(i) > length:
            new_nums.append(i)
    
    return list(set(new_nums))


print(majorityElement([1,2]))