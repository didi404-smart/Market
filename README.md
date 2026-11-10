# Market

Учебный проект на Python: консольная модель магазина с товарами, категориями и заказами. В проекте используются ООП, абстрактные классы, миксины, свойства, собственные исключения и тесты на `pytest`.

## Установка

```bash
git clone https://github.com/didi404-smart/Market
cd Market
poetry install
```

## Структура проекта

```
Market/
├── data/                   # json-файлы с категориями и товарами
├── src/
│   ├── base_category.py    # абстрактный родитель Category и Order
│   ├── base_product.py     # абстрактный родитель Product
│   ├── category.py         # класс Category
│   ├── lawn_grass.py       # класс LawnGrass (наследник Product)
│   ├── my_exception.py     # MyException и ZeroQuantity
│   ├── order.py            # класс Order
│   ├── print_mixin.py      # миксин PrintMixin
│   ├── product.py          # класс Product
│   ├── products_iterator.py# итератор по товарам категории
│   ├── read_data.py        # чтение json и создание объектов
│   └── smartphone.py       # класс Smartphone (наследник Product)
├── tests/                  # тесты pytest
├── pyproject.toml
└── .flake8
```

## Классы

### Product

Товар с атрибутами `name`, `description`, `price`, `quantity`. Наследуется от `BaseProduct` и `PrintMixin`.

- **Цена приватная**, доступ через геттер и сеттер.
  - Если новая цена `<= 0`, выводится «Цена не должна быть нулевая или отрицательная», цена не меняется.
  - Если цена понижается, запрашивается подтверждение (`y` - согласие, любой другой ответ - отмена).
- **Нулевое количество.** При создании товара с `quantity <= 0` выбрасывается `ValueError`.
- **`new_product(product: dict, products: list = None)`** - класс-метод, создаёт товар из словаря. Если в списке `products` уже есть товар с таким же названием (без учёта регистра и пробелов), количества складываются, цена берётся более высокая, возвращается существующий объект.
- **Сложение `+`** возвращает суммарную стоимость двух товаров с учётом остатков. Складывать можно только товары одного класса, иначе `TypeError`.
- **`__str__`** возвращает строку вида `Название, 80 руб. Остаток: 15 шт.`.

### Smartphone и LawnGrass

Наследники `Product` с дополнительными атрибутами.

| Класс | Дополнительные атрибуты |
|---|---|
| `Smartphone` | `efficiency`, `model`, `memory`, `color` |
| `LawnGrass` | `country`, `germination_period`, `color` |

### Category

Категория товаров. Наследуется от `BaseCategory`.

- Список товаров приватный.
- `add_product(product)` добавляет объект `Product` или его наследника.
  - Для другого типа выбрасывается `TypeError`.
  - Для товара с нулевым количеством выбрасывается и перехватывается `ZeroQuantity`, выводится сообщение.
  - При успехе выводится сообщение о добавлении, а при любом исходе - «Обработка добавления товара завершена».
- `products` - геттер, возвращает строку с описанием всех товаров.
- `products_list` - геттер, возвращает список объектов `Product`.
- `total_cost` - стоимость всех товаров с учётом остатков.
- `average_price()` - средняя цена товаров категории, для пустой категории возвращает `0.0`.
- `__str__` возвращает название категории и общее количество товаров.
- Счётчики `category_count` и `product_count` общие для всех категорий.

### Order

Заказ с одним товаром. Наследуется от `BaseCategory`.

- Хранит товар, количество и итоговую стоимость (`total_cost`).
- Для не-товара выбрасывается `TypeError`, для количества `<= 0` - `ZeroQuantity`.
- Как и в `Category`, выводятся сообщения об успехе и о завершении обработки.

### ProductsIterator

Итератор по товарам категории: `for product in ProductsIterator(category)`.

### Абстрактные классы и миксин

- `BaseProduct` - родитель `Product` (абстрактные `new_product`, `__add__`, `__str__`).
- `BaseCategory` - родитель `Category` и `Order` (абстрактные `__init__`, `__str__`, `total_cost`).
- `PrintMixin` - при создании объекта печатает в консоль класс и параметры, например `Product(Название, 'Описание', 1200, 10)`.

### Исключения

- `MyException` - общий класс исключений проекта.
- `ZeroQuantity` - товар с нулевым количеством.

## Работа с json

Модуль `src/read_data.py`:

- `read_json(path)` читает json-файл, при отсутствии файла или неверном формате возвращает пустой список.
- `create_objective_json(data)` создаёт из данных объекты `Category` и `Product`.

```python
from src.read_data import read_json, create_objective_json

data = read_json("data/products.json")   # подставьте имя вашего файла
categories = create_objective_json(data)
```

## Пример использования

```python
from src.category import Category
from src.product import Product
from src.order import Order

phone = Product("Samsung Galaxy S23", "256GB, Серый", 180000.0, 5)
category = Category("Смартфоны", "Описание категории", [phone])

category.add_product(Product("Iphone 15", "512GB", 210000.0, 8))

print(category.products)
print(category)
print(category.average_price())

order = Order(phone, 2)
print(order)
```

## Тестирование

```bash
poetry run pytest
```

Отчёт о покрытии (HTML-версия создаётся в папке `htmlcov`):

```bash
poetry run pytest --cov=src --cov-report=html
```