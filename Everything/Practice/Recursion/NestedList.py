class NestedList:
    def __init__(self, list):
        self.list = list
    
    def flatten(self):
        res = []
        for element in self.list:
            if isinstance(element, int):
                res.append(element)
            elif isinstance(element, list):
                res.extend(NestedList(element).flatten())
        return res


    def sum(self):
        total = 0

        for el in self.list:
            if not isinstance(el, list):
                total += el
            elif isinstance(el, list):
                total += NestedList(el).sum()
                
        return total




nested = NestedList([1, [2, [3, 4], 5], [6]])
print(nested.flatten())  # Expected Output: [1, 2, 3, 4, 5, 6]
print(nested.sum())      # Expected Output: 21
