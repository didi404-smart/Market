import pytest

from src.my_exception import ZeroQuantity
from src.order import Order
from src.product import Product


def test_order_init(product2):
    order = Order(product2, 1)
    assert order.product is product2
    assert order.quantity == 1
    assert order.total_cost == 678
    assert order.name == "Cake"
    assert str(order) == "Заказ: Cake, количество: 1 шт., итого: 678 руб."


def test_order_wrong_product():
    with pytest.raises(TypeError):
        Order("не товар", 1)


def test_order_ok(capsys):
    order = Order(Product("A", "a", 10.0, 5), 2)
    assert order.total_cost == 20.0
    assert "Товар добавлен в заказ" in capsys.readouterr().out


def test_order_zero_quantity(fake_product, capsys):
    with pytest.raises(ZeroQuantity):
        Order(fake_product, 0)
    out = capsys.readouterr().out
    assert "Нельзя добавить продукт с нулевым количеством товара" in out
    assert "Товар добавлен в заказ" not in out
    assert "Обработка добавления товара завершена" in out
