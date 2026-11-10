class Book:
    def __init__(self, title, author, cost_price, selling_price, quantity):
        self.title = title
        self.author = author

        if cost_price < 0:
            raise ValueError("Cost price cannot be negative")

        if selling_price < 0:
            raise ValueError("Selling price cannot be negative")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.cost_price = cost_price
        self.selling_price = selling_price
        self.quantity = quantity

    # Calculate total inventory value
    def calculate_inventory_value(self):
        return self.cost_price * self.quantity

    # Update stock quantity
    def update_quantity(self, amount=1):
        if self.quantity + amount < 0:
            print(
                f"Error: Not enough stock of '{self.title}'. "
                f"Current stock: {self.quantity}"
            )
        else:
            self.quantity += amount
            print(
                f"Stock updated for '{self.title}'. "
                f"New quantity: {self.quantity}"
            )

    # Calculate total potential profit
    def calculate_profit(self):
        profit_per_book = self.selling_price - self.cost_price
        total_profit = profit_per_book * self.quantity
        return total_profit

    # Display book details
    def display_details(self):
        print("\n--- BOOK DETAILS ---")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Cost Price: KSh {self.cost_price:,.2f}")
        print(f"Selling Price: KSh {self.selling_price:,.2f}")
        print(f"Available Quantity: {self.quantity}")
        print(
            f"Inventory Value: "
            f"KSh {self.calculate_inventory_value():,.2f}"
        )
        print(
            f"Total Potential Profit: "
            f"KSh {self.calculate_profit():,.2f}"
        )


# Creating objects
book1 = Book("Python Basics", "John Smith", 1000, 1500, 10)
book2 = Book("Data Engineering", "Sarah Jones", 1800, 2500, 5)

# Display details
book1.display_details()
book2.display_details()

# Update stock: add 5 books
book1.update_quantity(5)

# Update stock: sell 3 books
book1.update_quantity(-3)

# Try selling more books than available
book1.update_quantity(-20)

# Display updated details
book1.display_details()
