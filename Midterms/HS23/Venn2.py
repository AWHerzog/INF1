
def venn(one, two, three):
    return (set(one) & set(two)) - set(three)



print( venn([1, 2, 2, 2, 3, 4], [2, 2, 3, 4], [3]))
print( venn([1.0, "hi", 3], [1.0, 3, "hi"], [3, 1]))
print( venn([1, 2, 3], [4, 5, 6], []))
print( venn([1, 2, 3], [1, 2, 3], [1, 2, 3]))