
def greetings(names):
    
    if not names:
        return "Hello?"
    
    if len(names) == 1:  
        return f"Hello, {names[0]}."
    
    if len(names) == 2:  
        return f"Hello, {names[0]} and {names[1]}."
    
    return f"Hello, {', '.join(names[:-1])} and {names[-1]}."
    
print(greetings([]))
print(greetings(['Josh']))
print(greetings(['Josh', 'Alice']))
print(greetings(['Josh', 'Alice', 'Marie']))
