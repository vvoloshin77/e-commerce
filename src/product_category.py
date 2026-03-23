import json


class Product:
    """Класс содержащий информацию о продукте"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс содержащий информацию о категории"""
    name: str
    description: str
    products: list
    products_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.products_count += len(self.products)
        Category.category_count += 1


if __name__ == '__main__':
    with open(r'C:\Users\usger\PycharmProjects\e_commerce\data\products.json', 'r', encoding='UTF-8') as f:
        product = json.load(f)
    categories = []
    for category_data in product:
        products = []
        for product_data in category_data['products']:
            product = Product(product_data['name'], product_data['description'], product_data['price'],
                              product_data['quantity'])
            products.append(product)
        category = Category(category_data['name'], category_data['description'], products)
        categories.append(category)

        print(product.name)
        print(product.description)
        print(product.price)
        print(product.quantity)

        print(category.name)
        print(category.description)
        print(category.products)