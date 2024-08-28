from supermarket import Supermarket

class Main:
    def __init__(self) -> None:
        print("---- Welcome to SNC Supermarket ----")
        # 1. Initialize
        supermarket = Supermarket('products.csv')
        supermarket.loadProduct()
        
        # 2. Operate
        supermarket.displayProducts()
        
        # 3. Cleanup
        print("Thank You for Shopping.")

if __name__ == "__main__":
    app = Main()
