from abc import ABC, abstractmethod

class Actor(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def get_monthly_salary(self):
        pass

    def get_name(self):
        return self.name

class Lead(Actor):
    unique_id = 0
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
        self.id = Lead.unique_id
        Lead.unique_id += 1
    
    def get_monthly_salary(self):
        return (self.salary / 12)

    def get_id(self):
        return self.id

    def __repr__(self):
        return f" Salary: {self.get_monthly_salary()} ({self.get_id})"

class Extra(Actor):
    def __init__(self, name, hsalary, hper_month):
        super().__init__(name)
        if hsalary < 9.4:
            raise ValueError("Hourly salary must be at least 9.4")
        self._hsalary = hsalary
        self._hper_month = hper_month
    
    def get_monthly_salary(self):
        return self._hsalary * self._hper_month
    
    def __repr__(self):
        return "Salary: {self.get_monthly_salary()} (temp)"


class Studio:
    def __init__(self, name):
        self.name = name
        self.actors = []
    
    def add_actor(self, actor):
        if actor in self.actors:
            raise ValueError("Actor already added to the studio")
        self.actors.append(actor)
        
    
    def get_monthly_staff_cost(self):
        return sum(actor.get_monthly_salary() for actor in self.actors)

e = Studio("Warmer Sisters")
i1 = Lead("Bob", 60000) # yearly salary
i2 = Lead("Alice", 75000) # yearly salary
i3 = Extra("Taylor", 21.50, 15) # hourly salary, hours per month
assert i1.get_name() == "Bob"
assert i3.get_name() == "Taylor"
assert i1.get_id() == 0
assert i2.get_id() == 1
assert i1.get_monthly_salary() > 4000
assert i3.get_monthly_salary() == 322.50
e.add_actor(i1)
e.add_actor(i2)
e.add_actor(i3)
assert e.get_monthly_staff_cost() > 9000