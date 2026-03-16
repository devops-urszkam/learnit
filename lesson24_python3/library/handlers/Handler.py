from abc import ABC, abstractmethod


class Handler(ABC):
    @abstractmethod
    def __init__(self, library: "Library"):
        self.library = library

    @staticmethod
    def _non_empty(value, field):
        cleaned = str(value).strip()
        if not cleaned:
            raise ValueError(f"{field} cannot be empty")
        return cleaned
