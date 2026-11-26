from src.cat_iterator import CategoryIterator  # pragma: no cover
from src.lawngrass import LawnGrass  # pragma: no cover
from src.product_category import Category, Product  # pragma: no cover
from src.smartphone import Smartphone  # pragma: no cover

if __name__ == "__main__":  # pragma: no cover
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(str(category1))

    print(category1.products)

    sp = Smartphone("iphone", "piece", 900, 4, "vg", "good", "256GB", "sky")

    print(sp)

    lg = LawnGrass("ork", "good ork", 7000, 99, "Australia", 6.7, "burgundy")

    print(lg)

    print("\n---Демонстрация работы итератора---")

    iterator = CategoryIterator(category1)

    for item in iterator:
        print(item)
