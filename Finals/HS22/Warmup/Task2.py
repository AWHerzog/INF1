
import string

def is_perfect_panagram(sentence, alphabet=string.ascii_lowercase):
    
    sentence = sentence.lower()
    letters=[]
    for c in sentence:
        if c in alphabet:
            letters.append(c)
    
    return len(letters) == len(set(letters)) == len(alphabet)
