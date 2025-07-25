"""Main module for the Best Buy store application.
This module initializes the store with products and provides a menu for user interaction."""
from products import Product
from store import Store


# setup initial stock of inventory
product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = Store(product_list)


def store_list(store_obj: Store):
    """Lists all products in the store."""
    print(f"{'-' * 6}")
    for product_num, product in enumerate(store_obj.get_all_products(), start=1):
        print(f"{product_num}. {product.show()}")
    print(f"{'-' * 6}")


def total_amount(store_obj: Store):
    """Shows the total amount of all products in the store."""
    print(f"Total of {store_obj.get_total_quantity()} items in store.")


def make_order(store_obj: Store):
    """Makes an order from the store."""
    shopping_list = []
    product_orders = []
    store_list(store_obj)
    print("When you want to finish order, enter empty text.")
    while True:
        product_num = input("Which product # do you want? ")
        product_amount = input("What amount do you want? ")
        if not product_num or not product_amount:
            break
        try:
            product_num = int(product_num)
            product_amount = int(product_amount)
            if product_num < 1 or product_num > len(store_obj.get_all_products()):
                raise ValueError("Product number out of range.")
        except ValueError as e:
            print(f"Error adding product! {e}")
            continue

        product = store_obj.get_all_products()[product_num - 1]

        for index, (prod, amount) in enumerate(shopping_list):
            if prod == product:
                print("Product already in list, adding amount to existing product.")
                shopping_list[index] = (prod, amount + product_amount)
                break
        if product.name not in product_orders:
            shopping_list.append((product, product_amount))
            product_orders.append(product.name)
            print("Product added to list!")

    if shopping_list:
        total_price = store_obj.order(shopping_list)
        if total_price > 0:
            print(f"{'*' * 10} Order made! {'*' * 10}\n Total payment: ${total_price:.2f}")


def exit_menu():
    """Exits the menu."""
    print("Exiting the menu, Goodbye!")
    exit()


# Menu dictionary
MENU = {1: {'description': "List all products in the store",
            'function': store_list},
        2: {'description': "Show total amount in store",
            'function': total_amount},
        3: {'description': "Make an order",
            'function': make_order},
        4: {'description': "Quit",
            'function': exit_menu}
            }


def start(store_obj: Store):
    """Main function to show menu and handle user input."""
    # Menu Loop
    while True:
        print(f"\n{'*' * 10} Store Menu {'*' * 10}\n")
        for key, value in MENU.items():
            print(f"{key}. {value['description']}")
        try:
            user_choice = int(input("\nEnter your choice (1-4): "))
            if user_choice in MENU:
                if user_choice != 4:
                    MENU[user_choice]['function'](store_obj)
                elif user_choice == 4:
                    MENU[user_choice]['function']()
            else:
                raise ValueError("Invalid choice, please select a number between 1 and 4.")
        except ValueError as e:
            print(f"Please enter a valid number (1-4): {e}")


if __name__ == "__main__":
    start(best_buy)
