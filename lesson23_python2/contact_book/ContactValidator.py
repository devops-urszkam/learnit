import re
from functools import wraps


class ContactValidator:
    @staticmethod
    def validate_name(field_name):
        def decorator(func):
            @wraps(func)
            def wrapper(self, value):
                if not value:
                    raise ValueError(f"{field_name} cannot be empty")
                if not re.fullmatch(r"(?:[^\W\d_]|[ -])+", value):
                    raise ValueError(f"{field_name} can contain only letters, spaces and hyphens")
                return func(self, value)

            return wrapper

        return decorator

    @staticmethod
    def validate_mobile(func):
        @wraps(func)
        def wrapper(self, value):
            if not re.fullmatch(r"\+?\d+", value):
                raise ValueError("Mobile can contain only digits with optional leading '+'")
            return func(self, value)

        return wrapper

    @staticmethod
    def validate_email(func):
        @wraps(func)
        def wrapper(self, value):
            if not re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)+", value):
                raise ValueError("Email has invalid format")
            return func(self, value)

        return wrapper
