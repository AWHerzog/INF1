import re

class ProfanityFilter:

    def __init__(self, keywords, template):
        self.keywords = sorted(keywords, key=len, reverse=True)
        self.template = template

    def clean(self, word):
        return (self.template * (len(word) // len(self.template) + 1))[:len(word)]

    def filter(self, msg):
        
        pattern = re.compile("|".join(re.escape(keyword) for keyword in self.keywords), re.IGNORECASE)

        def replace(match):
            return self.clean(match.group())

        return pattern.sub(replace, msg)


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
    offensive_msg = "abc defghi mastard jklmno"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklm