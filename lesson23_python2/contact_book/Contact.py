from ContactValidator import ContactValidator


class Contact:
    def __init__(self, contact_id, first_name, last_name, mobile, email):
        self._id = contact_id
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.email = email

    @property
    def id(self):
        return self._id

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    @ContactValidator.validate_name("first_name")
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    @ContactValidator.validate_name("last_name")
    def last_name(self, value):
        self._last_name = value

    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    @ContactValidator.validate_mobile
    def mobile(self, value):
        self._mobile = value

    @property
    def email(self):
        return self._email

    @email.setter
    @ContactValidator.validate_email
    def email(self, value):
        self._email = value

    def __str__(self):
        return (
            f"id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}', "
            f"mobile='{self.mobile}', email='{self.email}'"
        )
