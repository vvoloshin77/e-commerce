import pytest
from src.product_category import Product, Category

@pytest.fixture()
def products_smart():
    return Product('Самртфоны', 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни', 180000.0, 5)

def test_1(products_smart):
    assert products_smart.name == 'Самртфоны'
    assert products_smart.description == 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'
    assert products_smart.price == 180000.0
    assert products_smart.quantity == 5

@pytest.fixture()
def categories_smart():
    return Category('Iphone 15', '512GB, Gray space', '')

def test_2(categories_smart):
    assert categories_smart.name == 'Iphone 15'
    assert categories_smart.description == '512GB, Gray space'
    assert categories_smart.products == ''
