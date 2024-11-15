
class stringDict:
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