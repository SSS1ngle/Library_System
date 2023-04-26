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

