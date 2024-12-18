def compress(data):
    
    if not data:
        return ((), [])
    if len(data) > 0 and not data[0]:
        return ((), [()])
    
    keys = tuple(sorted(data[0].keys()))
    values_list = [tuple(dictionary[key] for key in keys) for dictionary in data]

    return (keys, values_list)



data = [
    {"a": 1, "b": 2, "c": 3},
    {"a": 4, "c": 6, "b": 5}
]
print(compress(data))