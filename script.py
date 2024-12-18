

class BinaryTree:
    def __init__(self ,key ,value=0, left = None,right=None):
        self.key = key
        self.left = left
        self.right = right
        
    def tally(self, needle):
        res = self.value if self.key == needle else -self.value
        if self.left != None:
            res += self.left.tally(needle)
        if self.right != None:
            res += self.right.tally(needle)
        return res