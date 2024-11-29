
class Data:
    def __init__(self, data):
        self.data = data

    def compute(self, function1, function2):
        return (function1(self.data), function2(self.data))
    

objects = [1.7, 2.3, 3, 4]
d = Data(objects)
print( d.data is objects )
print( d.compute(sum, min) )
print( d.compute(min, max) )