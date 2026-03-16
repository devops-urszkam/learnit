from abc import ABC, abstractmethod

class Admin(ABC):
    @abstractmethod
    def __init__(self, username, password, permissions: list[str] = []):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value
    
    @property
    def permissions(self):
        return list(self._permissions)

    @permissions.setter
    def permissions(self, value):
        self._permissions = value   
    
    def add_permission(self, permission):
        if permission not in self._permissions:
            self._permissions.append(permission)

    def remove_permission(self, permission):
        if permission in self._permissions:
            self._permissions.remove(permission)