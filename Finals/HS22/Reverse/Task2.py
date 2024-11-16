class Rider:
    def __init__(self, fname, lname, ticket_class):
        self.fname = fname
        self.lname = lname
        self.ticket_class = ticket_class

    def __repr__(self):
        
        if self.ticket_class == "Ga": class_str = "general ticket"
        if self.ticket_class == "D": class_str = "day ticket"
        if self.ticket_class == "M": class_str = "monthly ticket"
        return F"{self.fname} {self.lname}, {class_str}"

class Train:
    def __init__(self, registration, destination):
        self.registration = registration
        self.destination = destination
        self.riders = []
    
    def board(self, p):
        self.riders.extend(p)
    
    @staticmethod
    def parse_reservations(reservations):
        return [Rider(f,l,t) for (f,l,t) in [m.split(",") for m in reservations.split(",")]]
    
    def get_riders(self, ticket_class = None):
        if ticket_class == None:
            return None
        return [p for p in self.riders if p.ticket_class == ticket_class]