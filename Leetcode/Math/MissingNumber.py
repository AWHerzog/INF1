
def missingNumber(nums):

    x = len(nums)

    for i in range(0, x + 1):
        if i not in nums:
            return i




missingNumber([9,6,4,2,3,5,7,0,1])