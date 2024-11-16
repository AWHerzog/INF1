
class Hand:
    def __init__(self, cards):
        self.__cards = cards
    
    def __eq__(self, other):
        if not isinstance(other, Hand):
            return NotImplemented
        this = sum(self.__cards)
        that = sum(other.__cards)
        if 1 in self.__cards:
            this += 10
        if 1 in other.__cards:
            that += 10
        return this == that

print( Hand([1, 2]) == Hand([10, 3]) )
print( Hand([2, 5, 7]) == Hand([10, 4]) )
print( Hand([2, 5, 7]) != Hand([9]) )
print( Hand([2, 5, 7]) == "Flush" )