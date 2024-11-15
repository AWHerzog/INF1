
class BinaryTree:
    def __init__(self,key,value = 0, left=None,right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
    
    def tally(self, needle):
        res = 0
        if  needle == self.key:
            res += self.value
        else:
            res -=self.value

        if self.left:
            res += self.left.tally(needle)
        if self.right:
            res += self.right.tally(needle)
        return res

