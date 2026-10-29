from src.category import Category

class ProductsIterator:
    category: Category

    def __init__(self, category):
        self.category = category

    def __iter__(self):
        self.ind = 0
        return self

    def __next__(self):
        products = self.category.products_list()
        if self.ind < len(products):
            product = products[self.ind]
            self.ind += 1
            return product
        else:
            raise StopIteration
