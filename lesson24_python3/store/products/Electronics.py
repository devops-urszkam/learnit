from .Product import Product


class Electronics(Product):
    def __init__(self, name: str, price: float, code: str, brand: str):
        super().__init__(name, price, code)
        self.brand = brand

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, value: str) -> None:
        self._brand = value

    def calculate_discount(self) -> float:
        return 0.1 if self.price > 1000 else 0.05

    def __str__(self) -> str:
        return f"Electronics(name={self.name}, brand={self.brand}, price={self.price:.2f})"
