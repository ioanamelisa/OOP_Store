import json

from categories.category import Category
from products.product import Product

class Order:
    def __init__(self, category, destination_address):
        self.category = category
        self.destination_address = destination_address
        self.products_ordered = {}

    def add_product_to_order(self, product, quantity):
        if product.stock >= quantity:
            self.products_ordered[product] = quantity
            print(f"{quantity} {product.name} were added.")
        else:
            print(f"Insufficient stock for {product.name}.")

    def place_order(self):
        for product, quantity in self.products_ordered.items():
            product.reduce_stock(quantity)
            print(f"Ordered {quantity} {product.name}.")

    def display_order_summary(self):
        print("\nOrder Summary:")
        print(f"Destination Address: {self.destination_address}")
        for product, quantity in self.products_ordered.items():
            print(f"{quantity} pieces of {product.name}")

    def to_dict(self):
        products_list = [
            {'name': product.name, 'quantity': self.products_ordered.get(product, 0)}
            for product in self.category.products
        ]
        return {
            'category': self.category.name,
            'products': products_list,
            'destination_address': self.destination_address
        }

    def save(self, file_name):
        data = self.to_dict()
        try:
            with open(file_name, 'r') as file:
                orders = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            orders = []

        orders.append(data)

        with open(file_name, 'w') as file:
            json.dump(orders, file)




