from src.product import Product


def test_mixin_prints(capsys):
    Product("Cake", "Chocolate", 400, 3)
    assert capsys.readouterr().out == "Product(Cake, 'Chocolate', 400, 3)\n"
