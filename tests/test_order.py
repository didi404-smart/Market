from src.order import Order
import pytest

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

def test_order_wrong_quantity(product2):
    with pytest.raises(ValueError):
        Order(product2, -10)