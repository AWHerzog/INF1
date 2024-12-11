
def padded_zip(lists, padding=None):
    
    res = []
    
    for i in range(max(len(l) for l in lists)):
        this = []

        if padding is None:
            this = []

            for l in lists:
                try:
                    this.append(l[i])
                except IndexError:
                    this.append(padding)
            res.append(tuple(this))
    return tuple(res)



l1 = [1, 2, 3, 4, 5]
l2 = [1.5, 2.5, 3.5, 4.5]
l3 = ["please", "send", "help"]
print(padded_zip([l1, l2, l3]))
print(padded_zip([l1, l2, l3, l1], "!"))