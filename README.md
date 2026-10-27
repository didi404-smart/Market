# Market

Учебный проект: модели **Product** и **Category**, а также функции для чтения данных из JSON и создания объектов Python.

## Возможности

### Класс `Product`

- **Приватная цена.** Атрибут `price` доступен через геттер и сеттер.
  - Если новая цена `<= 0`, выводится сообщение «Цена не должна быть нулевая или отрицательная», цена не меняется.
  - Если цена понижается, программа запрашивает подтверждение (`y` - понизить, любой другой ответ - отмена).
- **`Product.new_product(product: dict, products: list = None)`** - класс-метод, создаёт товар из словаря.
  Если передан список `products` и в нём уже есть товар с таким же названием (без учёта регистра и пробелов), то количество складывается, а цена выбирается более высокая. В этом случае возвращается уже существующий объект.

### Класс `Category`

- **Приватный список товаров** `__products`, напрямую снаружи недоступен.
- **`add_product(product)`** - добавляет объект `Product` в категорию.
- **Геттер `products`** - возвращает строку вида `Название, 80 руб. Остаток: 15 шт.` для каждого товара.
- Счётчики `category_count` и `product_count` общие для всех категорий.

### Модуль `read_data.py`:
  - `read_json(path: str) -> list[dict]` — читает JSON-файл, при ошибке возвращает `[]`
  - `create_objective_json(data: list[dict]) -> list` — создаёт список объектов `Category` с товарами `Product`

## Структура проекта
```
.
├─ src/
│ ├─ init.py
│ ├─ product.py
│ ├─ category.py
│ └─ read_data.py
├─ tests/
│ ├─ init.py
│ ├─ conftest.py
│ ├─ test_product.py
│ ├─ test_category.py
│ └─ test_read_data.py
├─ products.json
├─ pyproject.toml
└─ README.md
```

## Установка:
1) Клонируйте репозиторий:
```commandline
git clone https://github.com/didi404-smart/BankProject.git
```
2) Установите poetry:
```commandline
pip install poetry
```
Установите зависимости:
```commandline
poetry install
```

