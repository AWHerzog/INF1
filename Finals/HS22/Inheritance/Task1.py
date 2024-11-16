from abc import ABC, abstractmethod

class Cookie:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

class Container(ABC):
    def __init__(self, contents):
        self.__contents = contents

    def get_price(self):
        return round(sum([w.get_price() for w in self.__contents]), 2)

    def get_contents(self):
        return self.__contents[:]

    @abstractmethod
    def get_number_of_cookies(self):
        pass

class Wrapper(Container):
    def __init__(self, cookies):
        super().__init__(cookies)
        if len(cookies) < 3 or len(cookies) > 5:
            raise Warning

    def get_number_of_cookies(self):
        return len(self.get_contents())

class Box(Container):
    seq = 1
    def __init__(self, wrappers):
        super().__init__(wrappers)
        if self.get_number_of_cookies() > 200:
            raise Warning
        self.__id = Box.seq
        Box.seq += 1

    def get_id(self):
        return self.__id

    def get_number_of_cookies(self):
        return sum([w.get_number_of_cookies() for w in self.get_contents()])

