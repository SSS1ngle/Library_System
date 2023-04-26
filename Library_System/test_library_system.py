from library_system import *

def test_library_system():
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