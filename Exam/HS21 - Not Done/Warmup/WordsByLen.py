
def words_by_len(sentence):
    if not isinstance(sentence, str):
        raise AssertionError

    words = sentence.split()  
    result = {}

    for word in words:
        word_length = len(word)
        if word_length not in result:
            result[word_length] = set()
        result[word_length].add(word)
    
    return result

    

print(words_by_len("Get well soon !!"))