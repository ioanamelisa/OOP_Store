from categories.category import Category
from categories.categories import Categories
from products.product import Product
from orders.order import Order
import json

if __name__ == "__main__":

    online_store = Categories()
    online_store.load_item('store_data.json')

    def list_all_categories():
        online_store.list_categories()

    def add_category():
        cat_name = input("Enter the name of the new category: ")
        category = Category(cat_name)
        online_store.add_category(category)
        online_store.save('store_data.json')
        print(f"The category '{cat_name}' has been added successfully.")

    def remove_category():
        cat_name = input("Enter the name of the category to remove: ")
        category = online_store.get_category_name(cat_name)
        if category:
            online_store.remove_category(cat_name)
            online_store.save('store_data.json')
            print(f"The category '{cat_name}' has been removed successfully.")
        else:
            print("Invalid category! Unable to remove.")

    def list_all_products():
        cat_name = input("Enter the name of the category: ")
        category = online_store.get_category_name(cat_name)
        if category:
            category.list_products()
        else:
            print("Invalid category! Unable to list products.")

    def add_product():
        cat_name = input("Enter the name of the category: ")
        category = online_store.get_category_name(cat_name)
        if category:
            prod_name = input("Enter the name of the new product: ")
            prod_price = float(input("Enter the price of the new product: "))
            prod_stock = int(input("Enter the stock of the new product: "))
            product = Product(prod_name, prod_price, prod_stock)
            category.add_product(product)
            online_store.save('store_data.json')
            print(f"The product '{prod_name}' has been added to the category '{cat_name}' successfully.")
        else:
            print("Invalid category! Unable to add product.")

    def remove_product():
        cat_name = input("Enter the name of the category: ")
        category = online_store.get_category_name(cat_name)
        if category:
            prod_name = input("Enter the name of the product to remove: ")
            category.remove_product(prod_name)
            online_store.save('store_data.json')
            print(f"The product '{prod_name}' has been removed from the category '{cat_name}' successfully.")
        else:
            print("Invalid category! Unable to remove product.")

    def list_all_orders():
        try:
            with open('store_orders.json', 'r') as file:
                orders = json.load(file)
                if orders:
                    print("All Orders:")
                    for order in orders:
                        print("\nOrder:")
                        category_name = order['category']
                        print(f"Category: {category_name}")
                        for product_data in order['products']:
                            print(f"Product: {product_data['name']} - Quantity: {product_data['quantity']}")
                        print(f"Destination Address: {order['destination_address']}")
                else:
                    print("No orders available.")
        except FileNotFoundError:
            print("No orders file found.")

    def new_order():
        destination_address = input("Enter the destination address for the new order: ")
        cat_name = input("Enter the name of the category for the new order: ")
        category = online_store.get_category_name(cat_name)
        if category:
            order = Order(category, destination_address)

            while True:
                prod_name = input("Enter the name of the product to add to the order (type 'ok' to finish your order): ")
                if prod_name.lower() == 'ok':
                    break
                product = category.get_product_name(prod_name)
                if product:
                    try:
                        quantity = int(input(f"Enter the quantity for {product.name}: "))
                        order.add_product_to_order(product, quantity)
                    except ValueError:
                        print("Invalid quantity.")
                else:
                    print("Product not found.")

            order.place_order()
            order.display_order_summary()

            order.save('store_orders.json')
            online_store.save('store_data.json')
            print("The order has been placed successfully.")

    menu = {
        '1': list_all_categories,
        '2': add_category,
        '3': remove_category,
        '4': list_all_products,
        '5': add_product,
        '6': remove_product,
        '7': list_all_orders,
        '8': new_order,
        '9': lambda: exit("Exiting the store."),
    }

    while True:
        print("\nStore options:")
        print("1. List all categories")
        print("2. Add a new category")
        print("3. Remove a category")
        print("4. List all products in a category")
        print("5. Add a new product to a category")
        print("6. Remove a product from a category")
        print("7. List all orders")
        print("8. Place a new order")
        print("9. Exit")

        choice = input("Enter your choice: ")
        action = menu.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please choose a number between 1 and 9.")
