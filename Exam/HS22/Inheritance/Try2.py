from abc import ABC, abstractmethod

class Cookie:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price

class Container:
    pass

class Wrapper:
    pass

class Box:
    pass

def make_cookies(n):
    return [Cookie("Chocolate", 0.50) if x % 2 == 0 else Cookie("Vanilla", 0.60) for x in range(n)]

cookies = make_cookies(4)
print(cookies[0].get_name())
print(cookies[0].get_price())

'''
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

'''