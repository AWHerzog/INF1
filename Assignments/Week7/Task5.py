class Publication:

    def __init__(self, authors, title, year):
        self.__authors = list(authors)  # Ensure immutability by copying the list
        self.__title = title
        self.__year = year

    # Getter methods to provide read-only access to private attributes
    def get_authors(self):
        return list(self.__authors)  # Return a copy of the list to ensure immutability

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    # Provide a representation of the class that matches its instantiation
    def __repr__(self):
        return f'Publication({repr(self.__authors)}, "{self.__title}", {self.__year})'

    # String representation matches the repr
    def __str__(self):
        return self.__repr__()

    # Equality operator (==)
    def __eq__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return (
            self.__authors == other.__authors and
            self.__title == other.__title and
            self.__year == other.__year
        )

    # Hash method to make Publication hashable, using tuple to ensure immutability
    def __hash__(self):
        return hash((tuple(self.__authors), self.__title, self.__year))

    # Less-than operator (<)
    def __lt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        # First compare authors
        if self.__authors != other.__authors:
            return self.__authors < other.__authors
        # If authors are the same, compare titles
        if self.__title != other.__title:
            return self.__title < other.__title
        # If titles are also the same, compare years
        return self.__year < other.__year

    # Less-than or equal-to operator (<=)
    def __le__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        # Delegate to < and ==
        return self < other or self == other

    # Greater-than operator (>)
    def __gt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        # Delegate to <=
        return not self <= other

    # Greater-than or equal-to operator (>=)
    def __ge__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        # Delegate to <
        return not self < other

# Testing the functionality
p1 = Publication(["A"], "B", 1234)
p2 = Publication(["A"], "B", 1234)
p3 = Publication(["B"], "C", 2345)

# Testing __str__ and __repr__
assert str(p1) == 'Publication([\'A\'], "B", 1234)', f"Expected: Publication(['A'], \"B\", 1234), got: {str(p1)}"

# Testing equality
assert p1 == p2, "p1 and p2 should be equal"
assert p2 != p3, "p2 and p3 should not be equal"

# Testing comparison operators
references = [
    Publication(["Gamma", "Helm", "Johnson", "Vlissides"], "Design Patterns", 1994),
    Publication(["Cockburn"], "Writing Effective Use Cases", 2000),
    Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
]

# Sorting should use the comparison methods defined
sorted_references = sorted(references)
expected_order = [
    Publication(["Cockburn"], "Writing Effective Use Cases", 2000),
    Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007),
    Publication(["Gamma", "Helm", "Johnson", "Vlissides"], "Design Patterns", 1994)
]

# Verify that the sorted list matches the expected order
assert sorted_references == expected_order, f"Sorting failed. Got: {sorted_references}"

# Print sorted references to verify visually
for ref in sorted_references:
    print(ref)


