import pytest
from src.product import Product

@pytest.fixture
def product1():
    return Product("Молоко", "Обезжиренное", 69.60, 10)

