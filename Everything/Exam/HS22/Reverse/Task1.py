
class Passengers:
    def __init__(self, fname, lname, ticket):
        self.fname = fname
        self.lname = lname
        self.ticket = ticket
    
    def __repr__(self):

        classes = {1: "1st class", 2: "Business class", 3: "economy class"}
        return f"{self.fname}, {self.lname}, {classes[self.ticket]}"

class Airplane:
    def __init__(self, model, i_d):
        self.model = model
        self.i_d = i_d
    
    def board(self, passengers):
        self.passengers = passengers

    def get_passengers(self, ticket_class=None):
        if ticket_class:
            return [p for p in self.passengers if p.ticket == ticket_class]
        return self.passengers
    
    @staticmethod
    def parse_manifest(manifest):
        passenger_list = []

        entries = manifest.split(";")

        for entry in entries:
            fname, lname, ticket = entry.split(",")
            passenger_list.append(Passengers(fname, lname, int(ticket)))

        return passenger_list
    
passengers = Airplane.parse_manifest(("Montgomery,Rich,1;Tim,Merchant,2;Sally,Sale,2;Peter,Poor,3"))
a = Airplane("A388", "G-XLEK")
a.board(passengers)
print(a.get_passengers())
p = a.get_passengers(2)
print(type(p[1]))
print(p[1])