from src.product import Product


def test_class_product(product1):
    assert product1.name == "Молоко"
    assert product1.description == "Обезжиренное"
    assert product1.price == 69.60
    assert product1.quantity == 10


def test_new_product(dict_product):
    p = Product.new_product(dict_product)

    assert isinstance(p, Product)
    assert p.name == dict_product["name"]
    assert p.description == dict_product["description"]
    assert p.price == dict_product["price"]
    assert p.quantity == dict_product["quantity"]


def test_new_product_no_duplicate(dict_product, product):
    other = dict_product | {"name": "iPhone"}

    p = Product.new_product(other, [product])

    assert p is not product
    assert p.name == "iPhone"
    assert product.quantity == 5


def test_new_product_duplicate_higher_price(dict_product, product):
    new_data = dict_product | {"price": 200000.0, "quantity": 3}

    p = Product.new_product(new_data, [product])

    assert p is product
    assert p.quantity == 8
    assert p.price == 200000.0


def test_price_setter_zero(product, capsys):
    product.price = 0

    assert "Цена не должна быть нулевая или отрицательная" in capsys.readouterr().out
    assert product.price == 180000.0


def test_price_setter_decrease_confirmed(product, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "y")

    product.price = 150000.0

    assert product.price == 150000.0


def test_price_setter_decrease_declined(product, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "n")

    product.price = 150000.0

    assert product.price == 180000.0


def test_str(product1):
    assert str(product1) == f"Молоко, 69.6 руб. Остаток: 10 шт.\n"


def test_add(product1, product2):
    assert product1 + product2 == 2730
