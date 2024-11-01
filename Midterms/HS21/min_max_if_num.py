
def min_max_of(values):
    
    numeric_values = [v for v in values if isinstance(v, (int, float))]

    
    if not numeric_values:
        return (None, None)
    
    
    min_value = min(numeric_values)
    max_value = max(numeric_values)

    
    if min_value == max_value:
        return (min_value, None)
    
    
    return (min_value, max_value)