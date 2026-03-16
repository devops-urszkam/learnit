from typing import Dict, List
from Book import Book
from Reader import Reader
from handlers.BookHandler import BookHandler
from handlers.ReaderHandler import ReaderHandler


class Library:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self._books: Dict[str, Book] = {}
        self._readers: Dict[str, Reader] = {}
        self.book_handler = None
        self.reader_handler = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def books(self):
        return self._books.copy()

    @property
    def readers(self):
        return self._readers.copy()

    # --- Książki ---
    def add_book(self, title: str, author: str, isbn: str, publication_year) -> Book:
        if isbn in self._books:
            raise ValueError(f"Book with ISBN {isbn} already exists.")
        self._books[isbn] = Book(title, author, isbn, publication_year)
        return self._books[isbn]

    def get_book(self, isbn: str) -> Book:
        book = self._books.get(isbn)
        if book is None:
            raise ValueError(f"Book with ISBN {isbn} not found.")
        return book

    def search_books(self, keyword: str, field: str = "title") -> List[Book]:
        field = field.lower()
        if field not in {"title", "author", "isbn"}:
            raise ValueError("Field must be one of: title, author, isbn")
        keyword = keyword.lower()
        return [
            book
            for book in self._books.values()
            if keyword in str(getattr(book, field)).lower()
        ]

    # --- Czytelnicy ---
    def register_reader(self, first_name: str, last_name: str, reader_id: str) -> Reader:
        if reader_id in self._readers:
            raise ValueError(f"Reader with id {reader_id} already exists.")
        self._readers[reader_id] = Reader(first_name, last_name, reader_id)
        return self._readers[reader_id]

    def get_reader(self, reader_id: str) -> Reader:
        reader = self._readers.get(reader_id)
        if reader is None:
            raise ValueError(f"Reader with id {reader_id} not found.")
        return reader

    # --- Operacje wypożyczeń ---
    def borrow_book(self, reader_id: str, isbn: str) -> Book:
        reader = self.get_reader(reader_id)
        book = self.get_book(isbn)
        reader.borrow_book(book)
        return book

    def return_book(self, reader_id: str, isbn: str) -> Book:
        reader = self.get_reader(reader_id)
        book = self.get_book(isbn)
        reader.return_book(book)
        return book

    def reader_loans(self, reader_id: str) -> list[Book]:
        reader = self.get_reader(reader_id)
        return [self._books[isbn] for isbn in reader.borrowed_books]

    def list_books(self) -> List[Book]:
        return list(self._books.values())

    def list_readers(self) -> List[Reader]:
        return list(self._readers.values())

    @classmethod
    def with_handlers(cls, name: str, address: str) -> "Library":
        lib = cls(name, address)
        lib.book_handler = BookHandler(lib)
        lib.reader_handler = ReaderHandler(lib)
        return lib
