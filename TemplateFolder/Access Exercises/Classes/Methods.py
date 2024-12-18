class Publication:

    def __init__(self, authors, title, year):
        self.__authors = tuple(authors)
        self.__title = title
        self.__year = year

    def __repr__(self):
        authors = "[" + ", ".join(f'"{author}"' for author in self.__authors) + "]"
        return f'Publication({authors}, "{self.__title}", {self.__year})'

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return (self.__authors == other.__authors and
                self.__title == other.__title and
                self.__year == other.__year)

    def __hash__(self):
        return hash((self.__authors, self.__title, self.__year))

    def get_authors(self):
        return list(self.__authors)

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    def __lt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        if self.__authors != other.__authors:
            return self.__authors < other.__authors
        if self.__title != other.__title:
            return self.__title < other.__title
        return self.__year < other.__year

    def __le__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return self < other or self == other

    def __gt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return not (self <= other)

    def __ge__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return not (self < other)

    def __ne__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return not self == other