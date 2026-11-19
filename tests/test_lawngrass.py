from src.lawngrass import LawnGrass
from src.product_category import Product


def test_lawn_grass_init(lawn_grass: LawnGrass) -> None:
    assert lawn_grass.name == "ork"
    assert lawn_grass.description == "good ork"
    assert lawn_grass.price == 7000
    assert lawn_grass.quantity == 99
    assert lawn_grass.country == "Australia"
    assert lawn_grass.germination_period == 6.7
    assert lawn_grass.color == "burgundy"
    assert isinstance(lawn_grass, Product)
