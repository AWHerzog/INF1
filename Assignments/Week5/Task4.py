import re

class ProfanityFilter:

    def __init__(self, keywords, template):
        # Sort offensive words by length in descending order
        self.keywords = sorted(keywords, key=len, reverse=True)
        self.template = template
    
    def clean(self, word):
        # Generate replacement string of the same length as the offensive word
        length = len(word)
        return (self.template * ((length // len(self.template)) + 1))[:length]
    
    def filter(self, msg):
        # Initialize the cleaned text as the input message
        text = msg

        # Replace each keyword with the cleaned version
        for word in self.keywords:
            pattern = re.compile(re.escape(word), re.IGNORECASE)
            text = pattern.sub(self.clean(word), text)

        return text    

if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
    offensive_msg = "abc defghi mastard jklmno"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  
