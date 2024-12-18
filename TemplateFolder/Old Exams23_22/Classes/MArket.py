import random

class Market:
    def __init__(self):
        self.__vendors = []
        self.__hour = 0
        self.__profits = 0

    def stats(self):
        return {
            "number of vendors": len(self.__vendors),
            "hour": self.__hour,
            "hourly profit": sum(self.__vendors),
            "total profit": self.__profits
        }

    def add_vendor(self, fee):
        self.__vendors.append(fee)

    def remove_vendor(self, fee):
        if fee not in self.__vendors:
            raise Warning
        self.__vendors.remove(fee)

    def progress_hour(self):
        self.__profits += sum(self.__vendors)
        self.__hour += 1