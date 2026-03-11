from abc import ABC, abstractmethod
from typing import Any


class Product(ABC):
    def __init__(self, name: str, price: float, code: str):
        self.name = name
        self.price = price
        self.code = code

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:  
        self._name = value 
    
    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, value: float) -> None:
        self._price = value 

    @property
    def code(self) -> str:
        return self._code

    @code.setter
    def code(self, value: str) -> None:
        self._code = value

    def calculate_price_with_discount(self) -> float:
        discount = self.calculate_discount()

        return self.price * (1 - discount)

    @abstractmethod
    def calculate_discount(self) -> float:
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name}, price={self.price:.2f}, code={self.code})"
