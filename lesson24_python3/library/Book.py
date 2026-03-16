class Book:
    def __init__(self, title: str, author: str, ISBN: str, publication_year: int, is_available: bool = True):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.publication_year = publication_year
        self.is_available = is_available
        self._borrower_id = None

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def ISBN(self):
        return self._ISBN

    @ISBN.setter
    def ISBN(self, value):
        self._ISBN = value

    @property
    def publication_year(self):
        return self._publication_year

    @publication_year.setter
    def publication_year(self, value):
        self._publication_year = value

    @property
    def is_available(self):
        return self._is_available

    @is_available.setter
    def is_available(self, value):
        self._is_available = value

    @property
    def borrower_id(self):
        return self._borrower_id

    def _borrow(self, reader_id: str) -> None:
        if not self.is_available:
            raise ValueError(f"Book '{self.title}' is already borrowed.")
        self.is_available = False
        self._borrower_id = reader_id

    def _return_book(self) -> None:
        if self.is_available:
            raise ValueError(f"Book '{self.title}' is not borrowed.")
        self.is_available = True
        self._borrower_id = None
