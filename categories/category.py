class Category:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        self.products = [p for p in self.products if p.name != product_name]

    def list_products(self):
        for product in self.products:
            print(f"{product.name} - Price: {product.price} - In Stock: {product.stock}")

    def get_product_name(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product
        return None

    def to_dict(self):
        products_list = [product.to_dict() for product in self.products]
        return {
            'name': self.name,
            'products': products_list
        }