import json

from src.category import Category
from src.product import Product
from src.read_data import create_objective_json, read_json


def test_read_json(tmp_path, data):
    p = tmp_path / "data.json"
    p.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    result = read_json(str(p))
    assert result == data

    res = read_json("this_file_does_not_exist_123.json")
    assert res == []

    p = tmp_path / "bad.json"
    p.write_text("{ not a json }", encoding="utf-8")
    result = read_json(str(p))
    assert result == []


def test_create_objective_json(data):
    categories = create_objective_json(data)
    assert isinstance(categories, list)
    assert len(categories) == 1

    cat = categories[0]
    assert isinstance(cat, Category)
    assert cat.name == "Phones"
    assert cat.description == "Smartphones"

    assert isinstance(cat.products, list)
    assert len(cat.products) == 2
    assert all(isinstance(p, Product) for p in cat.products)

    assert cat.products[0].name == "iPhone"
    assert cat.products[0].price == 1000.0
    assert cat.products[0].quantity == 3
