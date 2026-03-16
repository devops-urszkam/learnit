from typing import Set


class Reader:
    def __init__(self, first_name: str, last_name: str, reader_id: str):
        self.first_name = first_name
        self.last_name = last_name
        self.reader_id = reader_id
        self._borrowed_books: Set[str] = set()

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def reader_id(self):
        return self._reader_id

    @reader_id.setter
    def reader_id(self, value):
        self._reader_id = value

    @property
    def borrowed_books(self) -> Set[str]:
        return set(self._borrowed_books)

    def borrow_book(self, book: "Book") -> None:
        if not book.is_available:
            raise ValueError(f"Book '{book.title}' is not available.")
        book.borrow(self.reader_id)
        self._borrowed_books.add(book.ISBN)

    def return_book(self, book: "Book") -> None:
        if book.ISBN not in self._borrowed_books:
            raise ValueError(f"Reader {self.reader_id} does not have book '{book.title}'.")
        book.return_book()
        self._borrowed_books.remove(book.ISBN)
