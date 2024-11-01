
def shout(text):
    
    exclams = text.count("!")
    if exclams == 0: exclams = 1
    return text.upper() + exclams * "!"


print(shout("Hello, God"))