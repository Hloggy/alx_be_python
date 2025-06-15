# library_management.py

class Book:
    def _init_(self, title, author):  # ✅ fixed here
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_checked_out(self):
        return self._is_checked_out


class Library:
    def _init_(self):  # ✅ fixed here
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_checked_out():
                book.check_out()
                print(f"You checked out '{book.title}'.")
                return
        print(f"'{title}' is not available.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.is_checked_out():
                book.return_book()
                print(f"You returned '{book.title}'.")
                return
        print(f"'{title}' was not checked out.")

    def list_available_books(self):
        available_books = [book for book in self._books if not book.is_checked_out()]
        for book in available_books:
            print(f"{book.title} by {book.author}")

