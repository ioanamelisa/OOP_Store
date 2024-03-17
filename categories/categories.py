import json

from categories.category import Category
from products.product import Product

class Categories:
    def __init__(self):
        self.categories = []
        self.orders = []

    def list_categories(self):
        print("Categories:")
        for category in self.categories:
            print(category.name)

    def add_category(self, category):
        self.categories.append(category)

    def remove_category(self, category_name):
        self.categories = [c for c in self.categories if c.name != category_name]

    def get_category_name(self, category_name):
        for category in self.categories:
            if category.name == category_name:
                return category
        return None

    def to_dict(self):
        categories_list = [category.to_dict() for category in self.categories]
        orders_list = [order.to_dict() for order in self.orders]
        return {
            'categories': categories_list,
            'orders': orders_list
        }

    def save(self, file_name):
        data = self.to_dict()
        with open(file_name, 'w') as file:
            json.dump(data, file)

    def load_item(self, file_name):
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
            for category_data in data.get('categories', []):
                category = Category(category_data['name'])
                for product_data in category_data['products']:
                    product = Product(product_data['name'], product_data['price'], product_data['stock'])
                    category.add_product(product)
                self.add_category(category)
        except FileNotFoundError:
            pass