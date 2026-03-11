from enum import Enum
from .Cart import Cart
from users.Customer import Customer


class OrderState(Enum):
    NEW = "new"
    PAID = "paid"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class Order:
    def __init__(self, cart: Cart, user: Customer, payment_method: str, state: OrderState = OrderState.NEW):
        self.cart = cart
        self.user = user
        self.payment_method = payment_method
        self.state = state

    @property
    def cart(self) -> Cart:
        return self._cart

    @cart.setter
    def cart(self, value: Cart) -> None:
        self._cart = value

    @property
    def user(self) -> Customer:
        return self._user

    @user.setter
    def user(self, value: Customer) -> None:
        self._user = value

    @property
    def state(self) -> OrderState:
        return self._state

    @state.setter
    def state(self, value: OrderState | str) -> None:
        match value:
            case OrderState(): self._state = value
            case _: self._state = OrderState(value)

    @property
    def payment_method(self) -> str:
        return self._payment_method

    @payment_method.setter
    def payment_method(self, value: str) -> None:
        self._payment_method = value

    def __str__(self) -> str:
        return f"Order(state={self.state.value}, total={self.cart.calculate_total_price():.2f}, user={self.user.username})"
