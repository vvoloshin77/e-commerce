from src.product_category import Product
from src.smartphone import Smartphone


def test_smartphone_init(smartphone: Smartphone) -> None:
    assert smartphone.name == "iphone"
    assert smartphone.description == "piece"
    assert smartphone.price == 900
    assert smartphone.quantity == 4
    assert smartphone.efficiency == "vg"
    assert smartphone.model == "good"
    assert smartphone.memory == "256GB"
    assert smartphone.color == "sky"
    assert isinstance(smartphone, Product)
