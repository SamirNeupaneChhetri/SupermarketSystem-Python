import csv
from product import Product

class Supermarket:
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.products = []

    def loadProduct(self):
        try:
            with open(self.filepath, mode='r', encoding='UTF-8') as filehandle:
                csv_reader = csv.DictReader(filehandle)
                for row in csv_reader:
                    number = int(row['number'])
                    name = row['name']
                    category = row['category']
                    price = float(row['price'])
                    self.products.append(Product(number, name, category, price))
        except Exception as err:
            print(f"Failed to read file '{self.filepath}'.")
            print(err)
            exit(-1)

    def displayProducts(self):
        for product in self.products:
            product.display()
