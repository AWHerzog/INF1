class Book:
    def __init__(self, title, author):
        pass

class Library:
    def __init__(self):
        pass

    def add_book(self, title, author):
        pass

    def borrow_book(self, title):
        pass

    def return_book(self, title):
        pass

    def list_available_books(self):
        pass

# Example usage:
library = Library()
library.add_book("1984", "George Orwell")
library.add_book("To Kill a Mockingbird", "Harper Lee")
library.add_book("The Great Gatsby", "F. Scott Fitzgerald")

print("Available books:", library.list_available_books())

library.borrow_book("1984")
print("Available books after borrowing 1984:", library.list_available_books())

library.return_book("1984")
print("Available books after returning 1984:", library.list_available_books())
