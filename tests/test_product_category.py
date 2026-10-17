import pytest

from src.product_category import Category, Product


def test_product_init(products_smart: Product) -> None:
    assert products_smart.name == "Смартфоны"
    assert (
        products_smart.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert products_smart.price == 180000.0
    assert products_smart.quantity == 5


def test_price_setter_negative(capsys: pytest.CaptureFixture[str]) -> None:
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


def test_price_decrease_cancel(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
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


def test_price_decrease_accept(monkeypatch: pytest.MonkeyPatch) -> None:
    pr = Product(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        180000.0,
        5,
    )
    monkeypatch.setattr("builtins.input", lambda _: "y")
    pr.price = 100
    assert pr.price == 100


def test_new_product_existing() -> None:
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


def test_category_init(categories_smart: Category) -> None:
    assert categories_smart.name == "Iphone 15"
    assert categories_smart.description == "512GB, Gray space"
    assert categories_smart.products == ""


def test_add_product(categories_smart: Category, products_smart: Product) -> None:
    assert Category.products_count == 0
    categories_smart.add_product(products_smart)
    assert Category.products_count == 1
    assert "Смартфоны" in categories_smart.products
    assert "180000.0 руб." in categories_smart.products
    assert "Остаток: 5 шт." in categories_smart.products


def test_category_counters() -> None:
    Category("A", "B", [])
    Category("B", "D", [])
    assert Category.category_count == 2


def test_new_product_creates_new() -> None:
    p_list = [
        Product(
            "Смартфоны",
            "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
            180000.0,
            5,
        )
    ]
    new_dict = {
        "name": "Ноутбуки",
        "description": "Ноутбуки, как средство не только работы, но и получение дополнительных функций для удобства жизни",
        "price": 210000.0,
        "quantity": 9,
    }
    product = Product.new_product(new_dict, p_list)
    assert product.name == "Ноутбуки"
    assert (
        product.description
        == "Ноутбуки, как средство не только работы, но и получение дополнительных функций для удобства жизни"
    )
    assert product.price == 210000.0
    assert product.quantity == 9
    assert len(p_list) == 1
    assert product is not p_list[0]


def test_new_product_higher_price() -> None:
    pr_list = [
        Product(
            "Смартфоны",
            "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
            180000.0,
            5,
        )
    ]
    new_d = {
        "name": "Смартфоны",
        "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        "price": 210000.0,
        "quantity": 15,
    }
    product = Product.new_product(new_d, pr_list)
    assert product.name == "Смартфоны"
    assert (
        product.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert product.price == 210000.0
    assert product.quantity == 20
    assert len(pr_list) == 1
    assert product is pr_list[0]
