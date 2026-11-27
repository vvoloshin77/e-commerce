import pytest

from src.base_product import BaseProduct

def test_base_product():
    with pytest.raises(TypeError):
        BaseProduct()