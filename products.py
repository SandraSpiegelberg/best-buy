"""Product management module for a store.
This module defines the Product class, which represents a product in a store."""
class Product:
    """Class representing a product in a store. 
    The product has attributes such as name, price, quantity, 
    and if it is active or not."""
    def __init__(self, name: str, price: float | int, quantity: int):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if price < 0:
            raise ValueError("Price cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self) -> int:
        """Returns the current quantity of the product."""
        return self.quantity


    def set_quantity(self, quantity: int):
        """Sets the quantity of the product and deactivate the product if quantity is zero."""
        if not isinstance(quantity, int):
            raise TypeError("quantity must be an integer")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()


    def is_active(self) -> bool:
        """Returns whether the product is active."""
        return self.active


    def activate(self):
        """Activates the product."""
        self.active = True


    def deactivate(self):
        """Deactivates the product."""
        self.active = False


    def show(self) -> str:
        """Displays the product details."""
        return f"Product: {self.name}, Price: ${self.price}, Quantity: {self.quantity}"


    def buy(self, quantity: int) -> float:
        """Processes a purchase of the product, reducing the quantity and returning the total price."""
        if self.is_active():
            if not isinstance(quantity, int):
                raise TypeError("Quantity must be an integer")
            if quantity < 0:
                raise ValueError("Quantity cannot be negative")
            if self.quantity < quantity:
                raise ValueError("Not enough stock available")
            self.quantity -= quantity
            if self.quantity == 0:
                self.deactivate()
            return quantity * self.price
        else:
            raise ValueError("Product is not active, cannot buy")


def main():
    """Main function to check the functionality of the Product class."""
    bose = Product('Bose QuietComfort Earbuds', price=250, quantity=500)
    mac = Product('MacBook Air M2', price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    print(bose.show())
    print(mac.show())

    bose.set_quantity(1000)
    print(bose.show())

if __name__ == '__main__':
    main()
