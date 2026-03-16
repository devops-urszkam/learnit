from typing import Union
from .Product import Product


class Book(Product):
    def __init__(self, title: str, price: float, code: str, author: str, publication_year: Union[int, str]):
        super().__init__(title, price, code)
        self.author = author
        self.publication_year = publication_year

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value: str) -> None:
        self._author = value

    @property
    def publication_year(self) -> Union[int, str]:
        return self._publication_year
    
    @publication_year.setter
    def publication_year(self, value: Union[int, str]) -> None:
        self._publication_year = value

    def calculate_discount(self) -> float:
        return self.publication_year % 10 * 0.1

    def __str__(self) -> str:
        return f"Book(title={self.name}, author={self.author}, year={self.publication_year}, price={self.price:.2f})"
