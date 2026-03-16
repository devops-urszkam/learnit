from .Product import Product


class Clothing(Product):
    def __init__(self, name: str, price: float, code: str, size: str, brand: str):
        super().__init__(name, price, code)
        self.size = size
        self.brand = brand 

    @property
    def size(self) -> str:
        return self._size

    @size.setter
    def size(self, value: str) -> None:
        self._size = value

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, value: str) -> None:
        self._brand = value

    def calculate_discount(self) -> float:
        return 0.15 if self.brand.lower() == "premium" else 0.05

    def __str__(self) -> str:
        return f"Clothing(name={self.name}, brand={self.brand}, size={self.size}, price={self.price:.2f})"
