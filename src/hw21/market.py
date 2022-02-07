from __future__ import annotations

from products.product import Product
from products.apple import Apple
from products.banana import Banana
from products.cellery import Cellery
from products.strawbarry import Strawbarry


class ProductFactory:
    @staticmethod
    def get_prod(prod: str) -> Product:

        if prod == "Apple":
            return Apple()
        elif prod == "Banana":
            return Banana()
        elif prod == "Cellery":
            return Cellery()
        elif prod == "Strawbarry":
            return Strawbarry()
        else:
            raise Exception("This product is absent.")

if __name__ == "__main__":
    prod = input("Enter product:\n")
    product = ProductFactory.get_prod(prod)
    print(product)
