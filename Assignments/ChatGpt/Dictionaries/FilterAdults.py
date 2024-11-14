
def filter_adults(people):
    return {person["name"]: person["age"] for person in people if person["age"] >= 18}


people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 19},
    {"name": "David", "age": 15},
    {"name": "Eve", "age": 30}
]

result = filter_adults(people)
print(result)
