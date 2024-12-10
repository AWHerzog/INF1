
def transform_dict(data):
    
    return {key: value**2  if isinstance(value, int) else value.upper() if isinstance(value, str) else value for key, value in data.items()}


data = {
    "name": "Alice",
    "age": 25,
    "city": "wonderland",
    "temperature": 22.5,
    "count": 4
}

print(transform_dict(data))
# Expected Output:
# {
#     "name": "ALICE",
#     "age": 625,
#     "city": "WONDERLAND",
#     "temperature": 22.5,
#     "count": 16
# }
