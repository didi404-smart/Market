import pytest

from src.products_iterator import ProductsIterator


def test_iterator(product_iter):
    it = ProductsIterator(product_iter)
    assert it.ind == 0
    assert next(it).name == "Cake"
    assert it.ind == 1
    assert next(it).name == "Молоко"
    with pytest.raises(StopIteration):
        next(it)

    names = [p.name for p in ProductsIterator(product_iter)]
    assert names == ["Cake", "Молоко"]
