class Event:
    def __init__(self, name, seats):
        self.name = name
        self.seats = [None] * seats
    
    def enter(self, nmbr, person):
        if nmbr < 1 or nmbr > len(self.seats):
            raise IndexError("Seat number is out of bounds.")
        
        index = nmbr - 1

        if self.seats[nmbr] is not None:
            raise NameError
        
        self.seats[index] = person
    
    def get(self, num):
        if num < 1 or num > len(self.seats):
            raise IndexError("Seat number is out of bounds.")
        
        index = num - 1
        if self.seats[index] is None:
            return None
        
        return self.seats[index]
    
    def occupied(self):
        return len([seat for seat in self.seats if seat is not None])
    
    def empty(self):
        return len([seat for seat in self.seats if seat is None])
    
    def __lt__(self, other):
        return self.occupied() < other.occupied()

    def __gt__(self, other):
        return self.occupied() > other.occupied()

    def __eq__(self, other):
        return self.occupied() == other.occupied()
        
