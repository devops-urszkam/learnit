from products.Book import Book
from products.Electronics import Electronics
from products.Clothing import Clothing
from common.Cart import Cart
from common.Order import Order, OrderState
from users.Customer import Customer


def build_sample_order() -> Order:
    cart = Cart()
    cart.add_item(Book("Effective Python", 170.0, "B777434", "Brett Slatkin", 2021))
    cart.add_item(Electronics("4K TV", 4200.0, "E909242", "Sony"))
    cart.add_item(Clothing("Sneakers", 320.0, "C808434", "42", "Premium"))
    user = Customer("ula", "p@ssw0rd111")
    user.add_payment_info("Visa **** 1234")
    return Order(cart, user, payment_method="credit_card")


def main() -> None:
    order = build_sample_order()
    print(order)
    print(order.cart)
    for item in order.cart.items:
        print(f" - {item} -> after discount: {item.calculate_price_with_discount():.2f}")
    order.state = OrderState.PAID
    print(f"State updated: {order.state.value}")


if __name__ == "__main__":
    main()
