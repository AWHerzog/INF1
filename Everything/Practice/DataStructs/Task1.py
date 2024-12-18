data = {
    "name": "Alice",
    "details": {
        "age": 30,
        "address": {
            "city": "Wonderland",
            "zip": "12345"
        }
    },
    "preferences": {
        "food": "cake",
        "hobbies": {
            "indoor": "chess",
            "outdoor": "croquet"
        }
    },
    "age": 25
}

def nested_lookup(data, target_key):
    res = []

    if not isinstance(data, dict):
        return res

    for key, value in data.items():
        if key == target_key:
            res.append(value)  
        if isinstance(value, dict):
            res.extend(nested_lookup(value, target_key))
    
    return res


print(nested_lookup(data, "age"))
# Expected Output: [30, 25]

print(nested_lookup(data, "city"))
# Expected Output: ['Wonderland']

print(nested_lookup(data, "nonexistent"))
# Expected Output: []
