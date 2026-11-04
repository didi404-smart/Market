from src.product import Product


class Order:

    product: Product
    quantity: int

    def __init__(self, product, quantity):
        if not isinstance(product, Product):
            raise TypeError("В заказе должен быть объект Product или его наследник")
        if quantity < 0:
            raise ValueError("Количество должно быть положительным")

        self.product = product
        self.quantity = quantity
        self.__total_cost = quantity * product.price

    def __str__(self):
        return f"{self.name}, количество: {self.quantity} шт., итого: {self.total_cost} руб."

    @property
    def total_cost(self):
        return self.__total_cost