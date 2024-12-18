
from collections import defaultdict

# Dataset contains data that will be reverse indexed
dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
 ] 

def reverse_index(dataset):
    
    index_dictionary = defaultdict(list)

    for idx, string in enumerate(dataset):
        words = string.lower().split()
        
        for word in words:
            index_dictionary[word].append(idx)

    return dict(index_dictionary)

    # don't forget to return your resulting dictionary

# You can see the output of your function here
print(reverse_index(dataset))