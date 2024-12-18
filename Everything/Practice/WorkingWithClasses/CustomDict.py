
class CustomDict:
    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):
        self.data[key.upper()] = value

    def __getitem__(self, key):
        return self.data[key.upper()]
    
    def __delitem__(self, key):
        del self.data[key.upper()]
    
    def __contains__(self, key):
        return key.upper() in self.data  
    
    def __str__(self):
        return str(self.data)
    

d = CustomDict()
d["name"] = "Alice"
d["age"] = 30

print(d)           # Expected Output: {'NAME': 'Alice', 'AGE': 30'}
print(d["name"])   # Expected Output: 'Alice'
print("NAME" in d) # Expected Output: True
print("age" in d)  # Expected Output: True

del d["NAME"]
print(d)           # Expected Output: {'AGE': 30'}