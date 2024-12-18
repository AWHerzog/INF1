from abc import ABC, abstractmethod
import unittest

class Product(ABC):
    @abstractmethod
    def get_price(self):
        pass

class Bottle(Product):
    def __init__(self, price, name):
        self.price = price
        self.name = name

    def get_price(self):
        return self.price

class Crate(Product):
    def __init__(self):
        self._bottles = []
        self._max_size = 20

    def add(self, bottle):
        if len(self._bottles) >= self._max_size:
            raise RuntimeError("Crate capacity exceeded")
        self._bottles.append(bottle)

    def get_size(self):
        return len(self._bottles)

    def get_price(self):
        return sum(bottle.get_price() for bottle in self._bottles)

class FixedPriceCrate(Crate):
    def __init__(self, fixed_price):
        super().__init__()
        self._fixed_price = fixed_price

    def get_price(self):
        return self._fixed_price

class DiscountCrate(Crate):
    def get_price(self):
        total_price = super().get_price()
        discount = min(0.25, 0.02 * len(self._bottles))
        return round(total_price * (1 - discount), 2)

class ShopTestSuite(unittest.TestCase):
    def test_crate_add(self):
        c = Crate()
        c.add(Bottle(4.50, "Light Beer"))
        self.assertEqual(c.get_size(), 1)

    def test_crate_max_size(self):
        c = Crate()
        for _ in range(20):
            c.add(Bottle(4.00, "Strong Stuff"))
        with self.assertRaises(RuntimeError):
            c.add(Bottle(4.50, "Extra Bottle"))

    def test_crate_price(self):
        c = Crate()
        bottles = [Bottle(3.50, "Light Beer"), Bottle(4.50, "Passable Wine")]
        for b in bottles:
            c.add(b)
        self.assertEqual(c.get_price(), 8.00)

    def test_discount_crate_price(self):
        c = DiscountCrate()
        bottles = [Bottle(3.50, "Light Beer"), Bottle(4.50, "Passable Wine"), Bottle(4.00, "Strong Stuff")]
        for b in bottles:
            c.add(b)
        self.assertEqual(c.get_price(), 9.40)

    def test_fixed_price_crate(self):
        c = FixedPriceCrate(11.11)
        bottles = [Bottle(3.50, "Light Beer"), Bottle(4.50, "Passable Wine")]
        for b in bottles:
            c.add(b)
        self.assertEqual(c.get_price(), 11.11)

