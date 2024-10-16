def hamming_dist(signal_1, signal_2):
    
    if not signal_1["data"] or not signal_2:
        return "Empty signal on at least one of the sensors"
    if len(signal_1["data"]) != len(signal_2):
        return "Empty signal on at least one of the sensors"
    
    results = []
    for str1, str2 in zip(signal_1["data"], signal_2):
        
        if len(str1) != len(str2):
            return "Sensor defect detected"
        
        hamming_distance = sum(1 for a, b in zip(str1, str2) if a != b)
        
        
        if hamming_distance > 0:
            results.append((str1, str2, hamming_distance))

    return results
