class Robot:
    def __init__(self):
        
        self.x = 0
        self.y = 0

    def move(self, direction):
       
        if direction == "u":
            self.y += 1 
        elif direction == "d":
            self.y -= 1 
        elif direction == "l":
            self.x -= 1  
        elif direction == "r":
            self.x += 1  

    def get_position(self):
        
        return (self.x, self.y)


r = Robot()
r.move("u")
r.move("r")
r.move("r")
print(r.get_position()) 
