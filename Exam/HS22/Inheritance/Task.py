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
    
    def __init__(self):
        pass

    @abstractmethod
    def get_price(self):
        pass
    @abstractmethod
    def get_contents(self):
        pass

class Wrapper(Container):
    
    def __init__(self, cookies):
        if not (3 <= len(cookies) <= 5):
            raise Warning ("Invalid Cookie amount")
        self.cookies = cookies

    def get_contents(self):
        return self.cookies

    def get_price(self):
        return round(sum(cookie.get_price() for cookie in self.cookies), 2)


class Box(Container):
    _id_counter = 1

    def __init__(self, wrappers):
        total_cookies = sum(len(wrapper.get_contents()) for wrapper in wrappers)
        if total_cookies > 200:
            raise Warning("A box can contain at most 200 cookies.")
        self.wrappers = wrappers
        self.id = Box._id_counter
        Box._id_counter += 1

    def get_contents(self):
        return [cookie for wrapper in self.wrappers for cookie in wrapper.get_contents()]

    def get_number_of_cookies(self):
        return sum(len(wrapper.get_contents()) for wrapper in self.wrappers)

    def get_price(self):
        return round(sum(wrapper.get_price() for wrapper in self.wrappers), 2)

    def get_id(self):
        return self.id




def make_cookies(n):
    return [Cookie("Chocolate", 0.50) if x % 2 == 0 else Cookie("Vanilla", 0.60) for x in range(n)]

cookies = make_cookies(4)
print(cookies[0].get_name())
print(cookies[0].get_price())

w1 = Wrapper(cookies)
print([c.get_name() for c in w1.get_contents()])

w2 = Wrapper(make_cookies(4))
b = Box([w1, w2])
print(f"\nCookies in box: {b.get_number_of_cookies()}")
print(f"  Price of box: {b.get_price()}")
print(f"     ID of box: {b.get_id()}\n")

more_wrappers = [Wrapper(make_cookies(4)) for x in range(52)] # 208 cookies
try:
    overfull = Box(more_wrappers)
except Warning:
    print("Too many cookies for one box\n")



