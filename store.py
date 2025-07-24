"""Store module for managing products in a store.
This module defines the Store class, which """
from products import Product

class Store:
    """Class representing a Store that contains a list of all existing products."""
    def __init__(self, product_list):
        if not isinstance(product_list, list):
            raise TypeError("product_list must be a list")
        if not all(isinstance(product, Product) for product in product_list):
            raise TypeError("all items in product_list must be instances of Product")
        self.product_list = product_list


    def add_product(self, product: Product):
        """Adds a product to the store"""
        if not isinstance(product, Product):
            raise TypeError("The added product must be an instance of Product")
        self.product_list.append(product)


    def remove_product(self, product: Product):
        """Removes a product from the store"""
        if not isinstance(product, Product):
            raise TypeError("The removed product must be an instance of Product")
        if product in self.product_list:
            self.product_list.remove(product)
        else:
            raise ValueError("Product not found in the store")


    def get_total_quantity(self) -> int:
        """Returns the total quantity of all products in the store."""
        total_quantity = 0
        for product in self.product_list:
            total_quantity += product.get_quantity()
        return total_quantity


    def get_all_products(self) -> list[Product]:
        """Returns a list of all products in the store that are active."""
        product_list = []
        for product in self.product_list:
            if product.is_active():
                product_list.append(product)
        return product_list


    def order(self, shopping_list: list[(Product, int)]) -> float:
        """Orders products from the store, change the quantity of the product,
        buys the products and returns the total price. shopping_list is a list of tuples 
        where each tuple has two items a Product and the quantity to buy."""
        total_price = 0
        for product, quantity in shopping_list:
            if not isinstance(product, Product):
                raise TypeError("Each item in shopping_list must be a Product")
            total_price += product.buy(quantity)
        return total_price


def main():
    """Main function to check the functionality of the Store class."""
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(products[0], 1), (products[1], 2)]))
    print(best_buy.get_total_quantity())

if __name__ == '__main__':
    main()
