from typing import Union
from .Handler import Handler


class BookHandler(Handler):
    def __init__(self, library):
        super().__init__(library)

    def add_book(self, title: str, author: str, isbn: str, publication_year: Union[int, str]):
        title = self._non_empty(title, "Title")
        author = self._non_empty(author, "Author")
        isbn = self._non_empty(isbn, "ISBN")
        publication_year = self._non_empty(publication_year, "Publication year")
        return self.library.add_book(title, author, isbn, publication_year)

    def borrow_book(self, reader_id: str, isbn: str):
        reader_id = self._non_empty(reader_id, "Reader id")
        isbn = self._non_empty(isbn, "ISBN")
        return self.library.borrow_book(reader_id, isbn)

    def return_book(self, reader_id: str, isbn: str):
        reader_id = self._non_empty(reader_id, "Reader id")
        isbn = self._non_empty(isbn, "ISBN")
        return self.library.return_book(reader_id, isbn)

    def search(self, keyword: str, field: str = "title"):
        field = self._non_empty(field, "Field").lower()
        if field not in {"title", "author", "isbn"}:
            raise ValueError("Field must be one of: title, author, isbn")
        keyword = self._non_empty(keyword, "Keyword")
        return self.library.search_books(keyword, field)

    def list_all(self):
        return self.library.list_books()
