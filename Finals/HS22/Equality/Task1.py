
class Hand:
    def __init__(self, cards):
        self.cards = cards
    
    def __eq__(self, other):
        pass

print( Hand([1, 2]) == Hand([10, 3]) )
print( Hand([2, 5, 7]) == Hand([10, 4]) )
print( Hand([2, 5, 7]) != Hand([9]) )
print( Hand([2, 5, 7]) == "Flush" )