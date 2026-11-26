import pytest

from src.lawngrass import LawnGrass
from src.product_category import Category, Product
from src.smartphone import Smartphone


@pytest.fixture(autouse=True)
def reset_counters() -> None:
    """Обнуляет счётчики класса перед каждым тестом"""
    Category.category_count = 0
    Category.products_count = 0


@pytest.fixture()
def products_smart() -> Product:
    return Product(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        180000.0,
        5,
    )


@pytest.fixture()
def categories_smart() -> Category:
    return Category("Iphone 15", "512GB, Gray space", [])


@pytest.fixture
def smartphone() -> Smartphone:
    return Smartphone("iphone", "piece", 900, 4, "vg", "good", "256GB", "sky")


@pytest.fixture
def lawn_grass() -> LawnGrass:
    return LawnGrass("ork", "good ork", 7000, 99, "Australia", 6.7, "burgundy")
