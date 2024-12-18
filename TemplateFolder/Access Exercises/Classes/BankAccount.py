class BankAccount:
    
    def __init__(self, owner, balance = 0.0):
        self._owner = owner
        self._balance = balance

    def deposit(self, amount):
        
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self._balance += amount

    def withdraw(self, amount):
        
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        
        self._balance -= amount

    def __str__(self):
        return f"Account owner: {self._owner}\nAccount balance: CHF {self._balance:.1f}"

    def __repr__(self):
        return f"BankAccount('{self._owner}', {self._balance})"