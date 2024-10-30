def venn(one, two, three):
    
    l1 = set(one)
    l2 = set(two)
    
    

    empty_list = []
    
    for num in l1:
        empty_list.append(num)
    for num in l2:
        empty_list.append(num)

    new_list = set(empty_list)
    
    for num in three:
        if num in new_list:
            new_list.remove(num)
    return new_list
    
    

print(venn([1, 2, 2, 2, 3, 4], [2, 2, 3, 4], [3]))
print( venn([1.0, "hi", 3], [1.0, 3, "hi"], [3, 1]))
print( venn([1, 2, 3], [4, 5, 6], []))
print( venn([1, 2, 3], [1, 2, 3], [1, 2, 3]))

#def venn(one, two, three):
    #return (set(one) | set(two)) - set(three)
    


