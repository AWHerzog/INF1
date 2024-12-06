
class Data:

    def __init__(self, data):
        self.data = data 

    def compute(self, function):
        return [function(d) for d in self.data ]
        

objects = [1.7, 2.3, 3, 4]
d = Data(objects)
print( d.data is objects )
print( d.compute(str) )
import math
print( d.compute(math.floor) )