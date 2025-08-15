# inventory_system.py
# Inventory System: Track store products with stock alerts, product addition, updates, and listing

class Product:
    store_name= "Inventory Store"  # Class variable for store name
    def __init__(self, name, price, stock):
        # Initialize product with name, price, and stock quantity
        self.name = name
        self.price = price
        self.stock = stock  # Stock quantity of the product
    def __str__(self):
        # String representation of the product
        return f"Product: {self.name}, Price: ${self.price:.2f}, Stock: {self.stock}"
    @staticmethod
    def store_info():
        # Static method to return store information
        return f"Welcome to {Product.store_name}!"
    
class Inventory(Product):
    def __init__(self):
        # Initialize the inventory with an empty product list
        super().__init__("Inventory", 0, 0)
        self.products = []  # List to store Product objects
        self.alerts={"Low Stock": 5, "Out of Stock": 0}  # Alerts for stock levels
    @property
    def total_value(self):
        # Calculate the total value of all products in stock
        return sum(product.price * product.stock for product in self.products)
    @classmethod
    def get_store_name(cls):
        # Get the store name
        return cls.store_name
    def add_product(self, name, price, stock):
        # Add a new product to the inventory
        try:
            price = float(price)
            stock = int(stock)
            # Check for duplicate product names
            if any(product.name == name for product in self.products):
                return f"Product '{name}' already exists."
            if price > 0 and stock >= 0 and name:
                self.products.append(Product(name, price, stock))
                return f"Added: {name}"
            return "Invalid Input"
        except ValueError:
            return "Price must be a number and stock must be an integer."
    def update_stock(self, index, new_stock):
        # Update stock for a product by index
        try:
            new_stock = int(new_stock)
            if new_stock >= 0:
                self.products[index].stock = new_stock
                return f"Updated stock for {self.products[index].name} to {new_stock}"
            return "Stock must be a non-negative integer."
        except (IndexError, ValueError):
            return "Invalid index or stock value."
    def low_stock_alert(self):
        # Generate alerts for products with low or out-of-stock levels
        result = "Low Stock Alerts:\n"
        for i, product in enumerate(self.products):
            if product.stock == self.alerts["Out of Stock"]:
                result += f"{i}: {product.name} - Out of Stock\n"
            elif self.alerts["Out of Stock"] < product.stock <= self.alerts["Low Stock"]:
                result += f"{i}: {product.name} - Stock: {product.stock}\n"
        return result
    def list_products(self):
        # List all products in the inventory
        result = "Product List:\n"
        for i, product in enumerate(self.products):
            result += f"{i}: {product}\n"
        return result
    def __str__(self):
        # String representation of the inventory
        return f"{self.store_name} - Total Value: ${self.total_value:.2f}"

def main():
    # Main program loop for menu-driven inventory management
    inventory = Inventory()  # Create an Inventory instance
    global store_name
    store_name = inventory.get_store_name()
    while True:
        print("1. Add Product")
        print("2. Update Stock")
        print("3. Low Stock Alert")
        print("4. List Products")
        print("5. Exit")
        choice = input("Enter choice (1-5): ").strip()
        if choice == "1":
            # Add a new product
            name = input("Enter product name: ").strip()
            price = input("Enter product price: ").strip()
            stock = input("Enter product stock: ").strip()
            print(inventory.add_product(name, price, stock))
        elif choice == "2":
            # Update stock for an existing product
            index = int(input("Enter product index to update: "))
            new_stock = input("Enter new stock quantity: ").strip()
            print(inventory.update_stock(index, new_stock))
        elif choice == "3":
            # Show low/out-of-stock alerts
            print(inventory.low_stock_alert())
        elif choice == "4":
            # List all products
            print(inventory.list_products())
        elif choice == "5":
            # Exit the program
            print("Exiting program.")
            break
        else:
            # Handle invalid menu choice
            print("Invalid choice! Please enter 1-5.")

if __name__ == "__main__":
    main()