import random

class Revolver:
    def __init__(self, cylinder_size):
        self.cylinder_size = cylinder_size
        self.current_position = 0
        self.cylinder = [False] * cylinder_size
        self.reload()

    def reload(self):
        self.cylinder = [False] * self.cylinder_size
        bullet_position = random.randint(0, self.cylinder_size - 1)
        self.cylinder[bullet_position] = True

    def trigger(self):
        if self.cylinder[self.current_position]:
            self.cylinder[self.current_position] = False
            self.current_position = (self.current_position + 1) % self.cylinder_size
            return "BANG!!!"
        else:
            self.current_position = (self.current_position + 1) % self.cylinder_size
            return "Click!"




    

