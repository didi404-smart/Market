from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.\n"

    def __add__(self, other):
        """Складывает цену двух продуктов(с учетом кол-ва на складе)"""
        if type(self) is type(other):
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        raise TypeError

    @classmethod
    def new_product(cls, product: dict, products: list = None):
        """Создаёт товар из словаря. Если в списке products уже есть товар
        с таким же названием, складывает количество и выбирает большую цену"""
        new_item = cls(**product)
        if products:
            for p in products:
                if p.name.lower().strip() == new_item.name.lower().strip():
                    p.quantity += new_item.quantity
                    p.price = max(new_item.__price, p.price)
                    return p
        return new_item

    @property
    def price(self):
        """Возварщает цену продукта"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Меняет старую цену на новую"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            ans = input(f"Вы хотите понизить цену с {self.__price} до {new_price}?(y/n)\n")
            if ans != "y":
                return
        self.__price = new_price
