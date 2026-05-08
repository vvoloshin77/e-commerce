import json

#from mypy.types import AnyType


class Product:
    """Класс содержащий информацию о продукте"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            message = input("Цена ниже предыдущей. Подтвердить изменения ? y/n: ")
            if message.lower() != "y":
                print("Корректировка цены отменена")
                return
        self.__price = new_price

    @classmethod
    def new_product(cls, prod_dic: dict, products_list: list) -> None:
        """Класс-метод сравнивающий товары по названию и складывающий остатки вместе, устанавливаю большую цену"""
        for product in products_list:
            if product.name == prod_dic["name"]:
                product.quantity += prod_dic["quantity"]

                if prod_dic["price"] > product.price:
                    product.price = prod_dic["price"]
                return product

        return cls(
            prod_dic["name"],
            prod_dic["description"],
            prod_dic["price"],
            prod_dic["quantity"],
        )


class Category:
    """Класс содержащий информацию о категории"""

    name: str
    description: str
    products: list
    products_count = 0
    category_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.products_count += len(self.__products)
        Category.category_count += 1

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.products_count += 1

    @property
    def products(self) -> None:
        products_str = ""
        for product in self.__products:
            products_str += f"\n{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    # @property
    # def products(self):
    #     return self.__products

    # def products_str(self):
    #     result = ""
    #     for product in self.__products:
    #         result += f"\n{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
    #     return result


if __name__ == "__main__":  # pragma: no cover
    with open(
        r"C:\Users\usger\PycharmProjects\e_commerce\data\products.json",
        "r",
        encoding="UTF-8",
    ) as f:
        product = json.load(f)
    categories = []
    for category_data in product:
        products = []
        for product_data in category_data["products"]:
            product = Product(
                product_data["name"],
                product_data["description"],
                product_data["price"],
                product_data["quantity"],
            )
            products.append(product)
        category = Category(
            category_data["name"], category_data["description"], products
        )
        categories.append(category)

        print(product.name)
        print(product.description)
        print(product.price)
        print(product.quantity)

        print(category.name)
        print(category.description)
        print(category.products)
