from src.base_category import BaseCategory
from src.my_exception import ZeroQuantity
from src.product import Product


class Order(BaseCategory):
    name: str
    description: str
    product: Product
    quantity: int

    def __init__(self, product, quantity):
        try:
            if not isinstance(product, Product):
                raise TypeError("В заказе должен быть объект Product или его наследник")
            if quantity <= 0:
                raise ZeroQuantity
        except ZeroQuantity as e:
            print(e)
            raise
        else:
            self.name = product.name
            self.description = product.description
            self.product = product
            self.quantity = quantity
            self.__total_cost = quantity * product.price
            print("Товар добавлен в заказ")
        finally:
            print("Обработка добавления товара завершена")

    def __str__(self):
        return f"Заказ: {self.name}, количество: {self.quantity} шт., итого: {self.total_cost} руб."

    @property
    def total_cost(self):
        """Возвращает стоимость заказа"""
        return self.__total_cost
