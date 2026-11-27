import pytest

from src.lawngrass import LawnGrass
from src.product_category import Product
from src.smartphone import Smartphone


def test_print_mixin(capsys: pytest.CaptureFixture[str]) -> None:
    Product(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        180000.0,
        5,
    )
    message = capsys.readouterr()
    assert (
        message.out.strip()
        == "Product('Смартфоны', 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни', 180000.0, 5)"
    )

    Smartphone("iphone", "piece", 900, 4, "vg", "good", "256GB", "sky")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone('iphone', 'piece', 900, 4)"

    LawnGrass("ork", "good ork", 7000, 99, "Australia", 6.7, "burgundy")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass('ork', 'good ork', 7000, 99)"
