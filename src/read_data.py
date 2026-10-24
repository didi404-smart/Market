import json
import os
from json import JSONDecodeError

from src.category import Category
from src.product import Product


def read_json(path: str) -> list[dict]:
    """Считывает json файл"""
    file_path = os.path.abspath(path)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except FileNotFoundError, JSONDecodeError:
        return []


def create_objective_json(data: list[dict]) -> list:
    """Создает объекты из json файла"""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories
