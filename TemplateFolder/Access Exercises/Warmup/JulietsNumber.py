wa_nrs = ["0781111119", "0792653913", "0797763139", "0792793193", "0781139022", "0764320165"]



def get_possible_nrs(n):
  

    if len(n) != 9:
        raise ValueError("Input must have 9 characters")
    
    if not n.startswith("07"):
        raise ValueError("Input must start with '07'")
    
    possible_nrs_for_juliet = []

    for i in range(len(n) + 1):
        for digit in "0123456789":

            possible_number = n[:i] + digit + n[i:]

            if possible_number in wa_nrs:
                possible_nrs_for_juliet.append(possible_number)

    possible_nrs_for_juliet = list(set(possible_nrs_for_juliet))  
    
    return possible_nrs_for_juliet

    # Don't forget to return your result

# For this particular number, the function should find the
# last element in wa_nrs
print(get_possible_nrs("076432165"))
