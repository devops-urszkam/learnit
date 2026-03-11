from abc import ABC, abstractmethod


class User(ABC):
    @abstractmethod
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value: str):
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value: str):
        self._password = value

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(username={self.username})"
