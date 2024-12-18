class BinaryTree:
    def __init__(self, key, value=0, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def tally(self, needle):
        res = self.value if self.key == needle else -self.value
        if self.left != None:
            res += self.left.tally(needle)
        if self.right != None:
            res += self.right.tally(needle)
        return res


class BinaryTree:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    def find(self, needle):
        res = [self.data] if self.key == needle else []
        if self.left != None:
            res.extend(self.left.find(needle))
        if self.right != None:
            res.extend(self.right.find(needle))
        return res