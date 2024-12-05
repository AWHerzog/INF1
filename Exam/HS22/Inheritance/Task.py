from abc import ABC, abstractmethod

class Cookie:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price

class Container(ABC):
    def __init__(self, content):
        self.content = content

    def get_content(self):
        return self.content

    def get_price(self):
        pass

    @abstractmethod
    def get_number_of_cookies(self):
        pass


class Wrapper(Container):
    pass

class Box(Container):
    pass


