
class Passenger:
    def __init__(self, fname, lname, ticket_class):
        self.fname = fname
        self.lname = lname
        self.ticket_class = ticket_class
    
    def __repr__(self):
        class_str = "1st"
        if self.ticket_class == 2: class_str = "business"
        if self.ticket_class == 3: class_str = "economy"
        return f"{self.fname} {self.lname}, {class_str} class"

class Airplane:
    def __init__(self, model, registration):
        self.model = model
        self.registration = registration
        self.classes = [[], [], []]
    @staticmethod
    def parse_manifest(manifest):
        return [Passenger(f, l, int(t)) for (f, l, t) in [m.split(",") for m in manifest.split(";")]]

    def board(self, passengers):
        for p in passengers:
            self.classes[p.ticket_class-1].append(p)

    def get_passengers(self, ticket_class=None):
        if ticket_class == None:
            res = []
            for c in self.classes:
                res.extend(c)
            return res
        return self.classes[ticket_class-1]
        

    