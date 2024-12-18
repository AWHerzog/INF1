def merge(a, b):
    
    if not a or not b:
        return []
    
    new_list = []
    
    max_length = max(len(a), len(b))

    for i in range(max_length):
        
        val_a = a[i] if i < len(a) else a[-1]
        val_b = b[i] if i < len(b) else b[-1]

        new_list.append((val_a, val_b))


    return new_list


print(merge([0, 1, 2], [5, 6]))
