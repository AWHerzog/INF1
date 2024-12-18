
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f"{self.title} ({self.year} by {self.author})"
    
    def __repr__(self):
        return f'Book("{self.title}", "{self.author}", "{self.year}")'
    
    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return (self.title, self.author, self.year) == (other.title, other.author, other.year)

# Create books
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("1984", "George Orwell", 1949)
book3 = Book("Brave New World", "Aldous Huxley", 1932)

# Print book details
print(book1)
# Expected Output: "1984 (1949) by George Orwell"

print(repr(book1))
# Expected Output: Book("1984", "George Orwell", 1949)

# Compare books
print(book1 == book2)  # Expected Output: True
print(book1 == book3)  # Expected Output: False

    