
def duplicates_of(lst, xs):
    
    dupes = []

    for i in xs:
        for j in lst:
            if i == j:
                dupes.append(i)

    return len(dupes)

print(duplicates_of([1, 1, 'hello', 3], [1, 'hello', 1]))
print(duplicates_of([True, True], [True]))