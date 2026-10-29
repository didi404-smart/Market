from src.product import Product


class Category:
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
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    def add_product(self, product: Product):
        """Добавляет продукт в категорию"""
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
