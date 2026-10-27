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

    def add_product(self, product):
        self.__products.append(product)

    @property
    def products(self):
        res = ""
        for product in self.__products:
            res += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return res


