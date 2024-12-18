
def split(text):
    
    sentence = text.split()
    return sentence


assert split("") == []
assert split("aaa") == ["aaa"]
assert split("a bbb cc") == ["a", "bbb", "cc"]

