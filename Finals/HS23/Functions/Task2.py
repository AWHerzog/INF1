
class Data:
    def __init__(self, data):
        self.data = data

    def compute(self, func1, func2):
        return (func1(self.data), func2(self.data))

objects = [1.7, 2.3, 3, 4]
d = Data(objects)
print( d.data is objects )
print( d.compute(sum, min))
print( d.compute(min, max))