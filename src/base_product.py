from abc import ABC, abstractmethod
from typing import Self


class BaseProduct(ABC):
    name: str
    description: str
    quantity: int

    @abstractmethod
    def __str__(self) -> str:
        pass #pragma: no cover

    @abstractmethod
    def __add__(self, other: Self) -> float:
        pass #pragma: no cover

    @classmethod
    @abstractmethod
    def new_product(cls, prod_dic: dict, products_list: list[Self]) -> Self:
        pass #pragma: no cover

    @property
    @abstractmethod
    def price(self) -> float:
        pass #pragma: no cover
