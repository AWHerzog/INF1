
def venn(one, two, three):
    return (set(one) | set(two)) - set(three)