class PrintMixin:

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name!r}, {self.description!r}, {self.price}, {self.quantity})"
