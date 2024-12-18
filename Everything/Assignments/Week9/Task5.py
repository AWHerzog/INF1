
def req_steps(num_disks):

    if num_disks == 1:
        return 1
    
    return 2 * req_steps(num_disks -1) + 1


print("For moving {} disks, {} steps are required.".format(3, req_steps(3)))