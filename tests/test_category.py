from src.category import Category
from src.product import Product


def test_class_category(category1, category2):
    assert category1.name == "Молочная продукция"
    assert category1.description == "Йогурты, молоко, творог"
    assert category1.products_list == ["Молоко 2.5%", "Творог 9%"]

    assert category2.category_count == 2
    assert category1.product_count == 5


def test_category_add_product(product, dict_product):
    cat = Category("Смартфоны", "Описание", [product])
    second = Product(**(dict_product | {"name": "iPhone"}))

    cat.add_product(second)

    assert "iPhone" in cat.products
    assert Category.product_count == 2


def test_category_products_getter(product):
    cat = Category("Смартфоны", "Описание", [product])

    assert cat.products == "Samsung, 180000.0 руб. Остаток: 5 шт.\n"


def test_category_empty_products():
    cat = Category("Пусто", "Нет товаров", [])

    assert cat.products == ""
