
def merge(nums1, m, nums2, n):
    
    nums1_trimmed = nums1[:m]

    nums1.clear()

    nums1.extend(nums1_trimmed)
    nums1.extend(nums2)

    nums1.sort()
    
    return nums1    



print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print(merge([1], 1, [], 0))
print(merge([0], 0, [1], 1))
