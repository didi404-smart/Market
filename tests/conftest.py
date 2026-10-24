import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product1():
    return Product("Молоко", "Обезжиренное", 69.60, 10)


@pytest.fixture
def category1():
    return Category("Молочная продукция", "Йогурты, молоко, творог", ["Молоко 2.5%", "Творог 9%"])


@pytest.fixture
def category2():
    return Category("Хлебные изделия", "Хлеб, баранки, булочки", ["Батон", "Слойка с сыром", "Пряники"])


@pytest.fixture
def data():
    return [
        {
            "name": "Phones",
            "description": "Smartphones",
            "products": [{"name": "iPhone", "description": "Apple phone", "price": 1000.0, "quantity": 3}],
        }
    ]
