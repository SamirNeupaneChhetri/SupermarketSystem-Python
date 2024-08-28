class Product:
    def __init__(self, number, name, category, price):
        self.number = number
        self.name = name
        self.category = category
        self.price = price

    def display(self):
        print(f"Product: {self.number}, Name: {self.name}, Category: {self.category}, Price: {self.price}")


