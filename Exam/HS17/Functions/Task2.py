
def compute_stats(lst):
    
    sorted_list = sorted(lst)

    sh = sorted_list[-2]

    average = sum(sorted_list) / len(sorted_list)

    median = 0

    n = len(sorted_list)
    if n % 2 == 0:  
        median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    else: 
        median = sorted_list[n // 2]

    return sh, int(average), median




stats = compute_stats([1,12,4,5,8])
assert stats[0] == 8 and stats[1] == 6 and stats[2] == 5

