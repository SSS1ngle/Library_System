from datetime import datetime


class Book():

    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.isbn = ISBN
        self.available = True


class Member():

    def __init__(self, name, adress, phone_number):
        self.name = name
        self.adress = adress
        self.phone_number = phone_number
        self.books_borrowed = []


class Library(Book, Member):

    def __init__(self):
        self.books = []
        self.members = []
        self.borrow_history = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member, book):
        if book in self.books and book.available:
            book.available = False
            member.books_borrowed.append(book)
            self.borrow_history.append({
                'member': member,
                'book': book,
                'date_borrowed': datetime.now()
            })

    def return_book(self, member, book):
        if book in member.books_borrowed:
            book.available = True
            member.books_borrowed.remove(book)
            for history in self.borrow_history:
                if history["member"] == member and history["book"] == book:
                    history["date_returned"] = datetime.now()

    def search_books(self, title=None, author=None):
        result = []
        for book in self.books:
            if (not title or book.title == title) and (not author or book.author == author):
                result.append(book)

        return result

    def get_borrowing_history(self, member):
        history = []
        for record in self.borrow_history:
            if record["member"] == member:
                history.append(record)

        history.sort(key=lambda x: x["date_borrowed"])
        return history


# Create some sample books
book1 = Book("The Catcher in the Rye", "J.D. Salinger", "0316769487")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "0446310786")
book3 = Book("1984", "George Orwell", "0451524934")

# Create a library and add the books to it
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Create some sample members
member1 = Member("Alice", "123 Main St", "555-1234")
member2 = Member("Bob", "456 Elm St", "555-5678")

# Add the members to the library
library.add_member(member1)
library.add_member(member2)

# Test borrowing and returning books
library.borrow_book(member1, book1)
assert book1.available == False
assert book1 in member1.books_borrowed

library.return_book(member1, book1)
assert book1.available == True
assert book1 not in member1.books_borrowed

# Test searching for books by title and author
results = library.search_books(title="1984")
assert len(results) == 1
assert results[0] == book3

results = library.search_books(author="Harper Lee")
assert len(results) == 1
assert results[0] == book2

# Test displaying member borrowing history
library.borrow_book(member1, book1)
library.borrow_book(member1, book2)
history = library.get_borrowing_history(member1)
