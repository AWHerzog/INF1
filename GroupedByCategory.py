
def group_by_category(data):
    return {category: sum(amount for c, amount in data if c == category) for category, _ in data}


data = [("fruit", 5), ("vegetable", 8), ("fruit", 3), ("meat", 10)]
print(group_by_category(data))  
# Expected: {"fruit": 8, "vegetable": 8, "meat": 10}