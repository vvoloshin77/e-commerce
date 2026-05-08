import pytest

from src.product_category import Category, Product


@pytest.fixture()
def products_smart() -> Product:
    return Product(
        "Самртфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        180000.0,
        5,
    )


def test_1(products_smart: Product) -> None:
    assert products_smart.name == "Самртфоны"
    assert (
        products_smart.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert products_smart.price == 180000.0
    assert products_smart.quantity == 5


def test_price_setter_negative(capsys, products_smart: Product) -> None:
    pr = Product(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        210000.0,
        6,
    )
    pr.price = -180000.0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert pr.price == 210000.0


def test_price_decrease_cancel(monkeypatch, capsys, products_smart: Product) -> None:
    pr = Product(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        210000.0,
        5,
    )
    monkeypatch.setattr("builtins.input", lambda _: "n")
    pr.price = 180000.0
    message = capsys.readouterr()
    assert message.out.strip() == "Корректировка цены отменена"
    assert pr.price == 210000.0


def test_price_decrease_accept(monkeypatch, products_smart: Product) -> None:
    pr = Product(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        180000.0,
        5,
    )
    monkeypatch.setattr("builtins.input", lambda _: "y")
    pr.price = 100
    assert pr.price == 100


def test_new_product(products_smart: Product) -> None:
    products_list = [
        Product(
            "Смартфоны",
            "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
            180000.0,
            5,
        )
    ]
    new_data = {
        "name": "Смартфоны",
        "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        "price": 180000.0,
        "quantity": 5,
    }
    product = Product.new_product(new_data, products_list)
    assert product.name == "Смартфоны"
    assert (
        product.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert product.price == 180000.0
    assert product.quantity == 10
    assert len(products_list) == 1


@pytest.fixture()
def categories_smart() -> Category:
    return Category("Iphone 15", "512GB, Gray space", [])


def test_2(categories_smart: Category) -> None:
    assert categories_smart.name == "Iphone 15"
    assert categories_smart.description == "512GB, Gray space"
    assert categories_smart.products == ""


def test_add_product() -> None:
    p = Category("Iphone 17 Pro Max", "2 TB, Midnight", [])
    assert p.name == "Iphone 17 Pro Max"
    assert p.description == "2 TB, Midnight"
    assert p.products == ""


def test_category_counters() -> None:
    Category("A", "B", [])
    Category("B", "D", [])
    assert Category.category_count >= 2
