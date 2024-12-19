
def padded_zip(lists, padding=None):
    # Find the length of the longest list
    max_length = max(len(lst) for lst in lists)
    
    # Create padded copies of each list
    padded_lists = [lst + [padding] * (max_length - len(lst)) for lst in lists]
    
    # Use zip to combine the lists into a tuple of tuples
    res = tuple(zip(*padded_lists))
    
    return res



l1 = [1, 2, 3, 4, 5]
l2 = [1.5, 2.5, 3.5, 4.5]
l3 = ["please", "send", "help"]
print(padded_zip([l1, l2, l3]))
print(padded_zip([l1, l2, l3, l1], "!"))