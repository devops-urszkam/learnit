from typing import List
from products.Product import Product


class Cart:
    def __init__(self):
        self._items: List[Product] = []

    @property
    def items(self) -> List[Product]:
        return self._items.copy()

    def add_item(self, product: Product) -> None:
        self._items.append(product)

    def remove_item(self, product: Product) -> None:
        if product in self._items:
            self._items.remove(product)
        else:
            raise ValueError("Product not found in cart.")

    def calculate_total_price(self) -> float:
        total_price = 0.0
        for product in self._items:
            total_price += product.calculate_price_with_discount()
        return total_price

    def __str__(self) -> str:
        return f"Cart(items={len(self._items)}, total={self.calculate_total_price():.2f})"
