from src.product import Product
from src.base_category import BaseCategory

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
        if not isinstance(product, Product):
            raise TypeError
        self.__products.append(product)
        Category.product_count += 1

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
