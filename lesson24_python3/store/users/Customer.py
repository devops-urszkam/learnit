from .User import User


class Customer(User):
    def __init__(self, username: str, password: str):
        super().__init__(username, password)
        self.orders = []
        self.payment_info = []

    @property
    def payment_info(self):
        return list(self._payment_info)
    
    @payment_info.setter
    def payment_info(self, value: list):
        self._payment_info = value
    
    @property
    def orders(self):
        return list(self._orders)

    @orders.setter
    def orders(self, value: list):
        self._orders = value

    def add_order(self, order) -> None:
        self._orders.append(order)

    def add_payment_info(self, payment_info) -> None:
        self._payment_info.append(payment_info) 

    def remove_payment_info(self, payment_info) -> None:
        if payment_info in self._payment_info:
            self._payment_info.remove(payment_info)
    
    def remove_order(self, order) -> None:
        if order in self._orders:
            self._orders.remove(order)

    def __str__(self) -> str:
        return f"Customer(username={self.username}, orders={len(self._orders)})"
    
