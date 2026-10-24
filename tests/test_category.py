from src.category import Category

def test_class_category(category1, category2):
    assert category1.name == "Молочная продукция"
    assert category1.description == "Йогурты, молоко, творог"
    assert category1.products == ["Молоко 2.5%", "Творог 9%"]

    assert category2.count_category == 2
    assert category1.count_products == 5