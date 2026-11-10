class MyException(Exception):
    """Общий класс для исключения"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Неизвестная ошибка"

    def __str__(self):
        return self.message


class ZeroQuantity(MyException):
    """Класс для исключений с нулевым количеством товара"""

    def __init__(self, message="Нельзя добавить продукт с нулевым количеством товара"):
        super().__init__(message)
