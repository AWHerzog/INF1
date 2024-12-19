from dataclasses import dataclass
 
@dataclass(frozen=True, unsafe_hash=True, order=True)
class Bill:
    denomination: int
 
class Account:
    def __init__(self, balance):
        self.balance = balance
    
    def __eq__(self, other):
        return self.balance == other
    
    def __repr__(self, other):
        if not isinstance(other, Account):
            return NotImplemented
        return ""
        #return f"[Account(Balance={self.balance}), Account(balance={Account.other.balance})]"
    
    def __lt__(self):
        pass
    def __gt__(self):
        pass
    def add(self):
        pass
    def balance(self):
        return self.balance

a1 = Account(10)
print(a1.balance)
print(a1 == "hello")
a2 = Account(100)
print([a1, a2])
b50 = Bill(50)
print(b50 )
print(a1 < a2)
print(a1 > a2)
print(a1 + b50)
print(a2 + b50)
a3 = a1 + a2
print(a3.balance)
print(a1.balance)