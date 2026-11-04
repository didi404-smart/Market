from src.product import Product
from src.base_category import BaseCategory

class Order(BaseCategory):
    name: str
    description: str
    product: Product
    quantity: int

    def __init__(self, product, quantity):
        if not isinstance(product, Product):
            raise TypeError("В заказе должен быть объект Product или его наследник")
        if quantity < 0:
            raise ValueError("Количество должно быть положительным")
        self.name = product.name
        self.description = product.description
        self.product = product
        self.quantity = quantity
        self.__total_cost = quantity * product.price

    def __str__(self):
        return f"Заказ: {self.name}, количество: {self.quantity} шт., итого: {self.total_cost} руб."

    @property
    def total_cost(self):
        return self.__total_cost