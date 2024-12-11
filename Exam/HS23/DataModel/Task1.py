
class StringDict:
    def __init__(self, elements=None):
        self.__elements = {}
        if elements:
            for k, v in elements.items():
                self.__elements[k] = str(v)

    def __len__(self):
        return len(self.__elements)

    def __eq__(self, other):
        return self.__elements == other.__elements

    def __setitem__(self, key, value):
        self.__elements[key] = str(value)

    def __getitem__(self, key):
        return self.__elements[key]

    def __str__(self):
        return str(self.__elements)

    def __repr__(self):
        return repr(self.__elements)

    def __contains__(self, thing):
        return thing in self.__elements

    
d1 = StringDict()
print(d1)
d1[1] = 100
d1["abc"] = print
print(d1)
print(isinstance(d1[1], str))
print(1 in d1)
print(100 in d1)
print(len(d1))
d2 = StringDict({"abc": print, 1: "100"})
d3 = StringDict({"abc": max})
print(d1 == d2)
print(d1 == d3)