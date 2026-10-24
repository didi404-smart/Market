import pytest
from src.product import Product
from src.category import Category

@pytest.fixture
def product1():
    return Product("Молоко", "Обезжиренное", 69.60, 10)

@pytest.fixture
def category1():
    return Category("Молочная продукция", "Йогурты, молоко, творог", ["Молоко 2.5%", "Творог 9%"])

@pytest.fixture
def category2():
    return Category("Хлебные изделия", "Хлеб, баранки, булочки", ["Батон", "Слойка с сыром", "Пряники"])