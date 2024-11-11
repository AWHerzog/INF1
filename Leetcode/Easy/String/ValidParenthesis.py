
def isValid(s):
    stack = []
    matching_pairs = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in matching_pairs:
            if not stack or stack[-1] != matching_pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0


            

print(isValid("()"))
print(isValid("[({})]"))