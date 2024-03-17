class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def to_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'stock': self.stock
        }

    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
        else:
            print(f"Error: Attempting to reduce stock for {self.name} beyond available quantity.")