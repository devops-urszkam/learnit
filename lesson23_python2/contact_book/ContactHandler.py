import pickle

from Contact import Contact


class ContactHandler:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, "_contact_book"):
            return
        self._contact_book = {}
        self._next_id = 1

    @classmethod
    def initialize(cls):
        return cls()
    
    def isEmpty(self):
        return not self._contact_book

    def add(self, first_name, last_name, email, mobile):
        new_contact = Contact(self._next_id, first_name, last_name, mobile, email)
        self._contact_book[self._next_id] = new_contact
        self._next_id += 1

        return new_contact
    
    def get_by_id(self, contact_id):
        return self._contact_book.get(contact_id)

    def get_all(self):
        return list(self._contact_book.values())

    def search_by_attribute(self, attribute, searched_val):
        searched = str(searched_val).strip().lower()
        
        return list(
            filter(
                lambda contact: getattr(contact, attribute, "").lower() == searched,
                self._contact_book.values(),
            )
        )

    def remove(self, contact_id):
        self._contact_book.pop(contact_id, None)

    def edit(self, contact_id, first_name=None, last_name=None, mobile=None, email=None):
        contact = self.get_by_id(contact_id)
        if contact is None:
            return
        if first_name is not None:
            contact.first_name = first_name
        if last_name is not None:
            contact.last_name = last_name
        if mobile is not None:
            contact.mobile = mobile
        if email is not None:
            contact.email = email

    def save(self, file_path="contacts.pkl"):
        with open(file_path, "wb") as file:
            pickle.dump(self._contact_book, file)

    def load(self, file_path="contacts.pkl"):
        with open(file_path, "rb") as file:
            self._contact_book = pickle.load(file)

        self._next_id = max(self._contact_book.keys(), default=0) + 1
