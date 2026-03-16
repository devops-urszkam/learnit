from .Handler import Handler


class ReaderHandler(Handler):
    def __init__(self, library):
        super().__init__(library)

    def register_reader(self, first_name: str, last_name: str, reader_id: str):
        first_name = self._non_empty(first_name, "First name")
        last_name = self._non_empty(last_name, "Last name")
        reader_id = self._non_empty(reader_id, "Reader id")
        return self.library.register_reader(first_name, last_name, reader_id)

    def list_readers(self):
        return self.library.list_readers()

    def loans(self, reader_id: str):
        reader_id = self._non_empty(reader_id, "Reader id")
        return self.library.reader_loans(reader_id)
