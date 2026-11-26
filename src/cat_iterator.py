from src.product_category import Category, Product


class CategoryIterator:

    def __init__(self, category_obj: Category) -> None:
        self.category_obj = category_obj
        self.index = 0

    def __iter__(self) -> "CategoryIterator":
        return self

    def __next__(self) -> Product:
        products_list = self.category_obj.product_list
        if self.index < len(products_list):
            lst = products_list[self.index]
            self.index += 1
            return lst
        else:
            raise StopIteration


# if __name__ == '__main__': # pragma: no cover
#     with open(
#         r"C:\Users\usger\PycharmProjects\e_commerce\data\products.json",
#         "r",
#         encoding="UTF-8",
#     ) as f:
#         data = json.load(f)
#     categories = []
#     for category_data in data:
#         products = []
#         for product_data in category_data["products"]:
#             prod = Product(
#                 product_data["name"],
#                 product_data["description"],
#                 product_data["price"],
#                 product_data["quantity"],
#             )
#             products.append(prod)
#
#             print(prod.name)
#             print(prod.description)
#             print(prod.price)
#             print(prod.quantity)
#
#         category = Category(category_data["name"], category_data["description"], products)
#         categories.append(category)
#
#         print(category.name)
#         print(category.description)
#         print(category.products)
#
#         iterator = CategoryIterator(category)
#
#         for item in iterator:
#             print(item)
