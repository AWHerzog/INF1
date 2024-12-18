def padded_zip(lists, padding=None):
    if not lists: return ()
    res = []
    for i in range(max(len(l) for l in lists)):
        this = []
        for l in lists:
            try:                       # if i < len(l):
                this.append(l[i])
            except IndexError:         # else:
                this.append(padding)
        res.append(tuple(this))
    return tuple(res)
