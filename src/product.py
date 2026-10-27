class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product:dict, products: list = None):
        """Создаёт товар из словаря. Если в списке products уже есть товар
        с таким же названием, складывает количество и выбирает большую цену"""
        new_item = cls(**product)
        if products:
            for p in products:
                if p.name.lower().strip() == new_item.name.lower().strip():
                    p.quantity += new_item.quantity
                    p.price = max(new_item.price, p.price)
                    return p
        return new_item