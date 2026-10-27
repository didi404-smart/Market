# Market

Учебный проект: модели **Product** и **Category**, а также функции для чтения данных из JSON и создания объектов Python.

## Возможности

- Класс `Product`:
  - `name` — название
  - `description` — описание
  - `price` — цена (`float`)
  - `quantity` — количество на складе (`int`)

- Класс `Category`:
  - `name` — название
  - `description` — описание
  - `products` — список товаров категории (объекты `Product`)
  - счётчики на уровне класса:
    - `Category.category_count` — количество созданных категорий
    - `Category.product_count` — общее количество товаров во всех созданных категориях

- Модуль `read_data.py`:
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

