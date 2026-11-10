from src.base_category import BaseCategory
from src.my_exception import ZeroQuantity
from src.product import Product


class Category(BaseCategory):
    name: str
    description: str
    __products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        count_product = 0
        for product in self.__products:
            count_product += product.quantity
        return f"{self.name}, количество продуктов: {count_product} шт."

    def add_product(self, product: Product):
        """Добавляет продукт в категорию"""
        try:
            if not isinstance(product, Product):
                raise TypeError
            if product.quantity <= 0:
                raise ZeroQuantity
        except ZeroQuantity as e:
            print(e)
        else:
            self.__products.append(product)
            Category.product_count += 1
            print("Товар добавлен в заказ")
        finally:
            print("Обработка добавления товара завершена")

    @property
    def products(self):
        """Возвразает строку с описанием продуктов в категории"""
        res = ""
        for product in self.__products:
            res += str(product)
        return res

    @property
    def products_list(self):
        """Список объектов для поиска дубликатов в Product.new_product."""
        return self.__products

    @property
    def total_cost(self):
        """Стоимость всех товаров категории с учётом остатков"""
        return sum(p.price * p.quantity for p in self.__products)

    def average_price(self):
        """подсчитывает средний ценник всех товаров в категории"""
        try:
            total = sum(product.price for product in self.__products)
            return total / len(self.__products)
        except ZeroDivisionError:
            return 0.0
