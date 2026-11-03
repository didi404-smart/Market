import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def product1():
    return Product("Молоко", "Обезжиренное", 69.60, 10)


@pytest.fixture
def product2():
    return Product("Cake", "Medovik", 678, 3)


@pytest.fixture
def category1():
    return Category("Молочная продукция", "Йогурты, молоко, творог", ["Молоко 2.5%", "Творог 9%"])


@pytest.fixture
def category2():
    return Category("Хлебные изделия", "Хлеб, баранки, булочки", ["Батон", "Слойка с сыром", "Пряники"])


@pytest.fixture
def product_iter():
    return Category(
        "Молочная продукция",
        "Йогурты, молоко, творог",
        [Product("Cake", "Medovik", 678, 3), Product("Молоко", "Обезжиренное", 69.60, 10)],
    )


@pytest.fixture
def data():
    return [
        {
            "name": "Phones",
            "description": "Smartphones",
            "products": [{"name": "iPhone", "description": "Apple phone", "price": 1000.0, "quantity": 3}],
        }
    ]


@pytest.fixture
def dict_product():
    return {
        "name": "Samsung",
        "description": "256GB",
        "price": 180000.0,
        "quantity": 5,
    }


@pytest.fixture
def product(dict_product):
    return Product(**dict_product)


@pytest.fixture(autouse=True)
def reset_counters(monkeypatch):
    monkeypatch.setattr(Category, "category_count", 0)
    monkeypatch.setattr(Category, "product_count", 0)


@pytest.fixture
def smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def lawn_grass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
