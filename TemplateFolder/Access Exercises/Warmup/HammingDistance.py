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


# The following lines print your function's output for an exemplary input to the console.
# Note that this does not include any of the mentioned edge cases for defective sensors or signals of different lenghts.
# Try to write your own tests for this.

signal_sensor_1 = {"times": [0, 1, 2, 3, 4, 5],
                   "data": ["00101110", "11001011", "11110000", "01000011", "11001101", "00011011"]}
signal_sensor_2 = ("00101110", "11001001", "11110011", "01111011", "11001101", "00011011")
print(hamming_dist(signal_sensor_1, signal_sensor_2))