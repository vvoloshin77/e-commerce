import json


class Product:
    """Класс содержащий информацию о продукте"""

    name: str
    description: str
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f'{self.name}, {self.__price:g} руб. Остаток: {self.quantity} шт.'

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
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
    def new_product(cls, prod_dic: dict, products_list: list["Product"]) -> "Product":
        """Класс-метод сравнивающий товары по названию и складывающий остатки вместе, устанавливаю большую цену"""
        for prod in products_list:
            if prod.name == prod_dic["name"]:
                prod.quantity += prod_dic["quantity"]

                if prod_dic["price"] > prod.price:
                    prod.price = prod_dic["price"]
                return prod

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
    products_count = 0
    category_count = 0

    def __init__(self, name: str, description: str, prod: list) -> None:
        self.name = name
        self.description = description
        self.__prod = prod
        Category.products_count += len(self.__prod)
        Category.category_count += 1

    def __str__(self) -> str:
        total_quantity = sum(prod.quantity for prod in self.__prod)
        return f'{self.name}, количество продуктов: {total_quantity} шт.'

    def add_product(self, prod: Product) -> None:
        self.__prod.append(prod)
        Category.products_count += 1

    @property
    def products(self) -> str:
        products_str = ""
        for pr in self.__prod:
            products_str += f"\n{pr.name}, {pr.price} руб. Остаток: {pr.quantity} шт.\n"
        return products_str


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
        category = Category(category_data["name"], category_data["description"], products)
        categories.append(category)

        print(product.name)
        print(product.description)
        print(product.price)
        print(product.quantity)

        print(category.name)
        print(category.description)
        print(category.products)
