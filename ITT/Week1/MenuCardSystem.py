class MenuCardSystem:
    def __init__(self):
        # Menu categorized
        self.menu = {
            "Starters / Snacks": {
                "Veg Spring Roll": 100,
                "Chicken Wings": 180,
                "French Fries": 90,
                "Paneer Tikka": 150
            },
            "Main Course": {
                "Burger": 120,
                "Pizza": 250,
                "Pasta": 200,
                "Veg Biryani": 180,
                "Chicken Biryani": 250,
                "Grilled Sandwich": 130
            },
            "Drinks": {
                "Coke": 50,
                "Lemonade": 40,
                "Coffee": 60,
                "Tea": 30
            },
            "Desserts": {
                "Ice Cream": 80,
                "Brownie": 120,
                "Gulab Jamun": 60
            }
        }
        self.orders = {}  # To store orders and quantities

    def display_menu(self):
        print("\n===== Menu Card =====")
        for category, items in self.menu.items():
            print("\n",category)
            for item, price in items.items():
                print(item ,"|", "Price:",price)

    def take_order(self):
        print("\nPlace your order! Type 'done' to finish.")
        while True:
            food_item = input("Enter Food Item: ").strip()
            if food_item.lower() == 'done':
                break

            # Check if the food item exists in any category
            found = False
            for items in self.menu.values():
                if food_item in items:
                    found = True
                    price = items[food_item]
                    break

            if not found:
                print("Item not available. Please choose from the menu.")
                continue

            try:
                quantity = int(input(f"Enter quantity for {food_item}: "))
                if quantity <= 0:
                    print("Quantity must be at least 1.")
                    continue
            except ValueError:
                print("Please enter a valid number for quantity.")
                continue

            if food_item in self.orders:
                self.orders[food_item] += quantity
            else:
                self.orders[food_item] = quantity

    def display_bill(self):
        if not self.orders:
            print("\nNo items ordered.")
            return
        print("\n===== Bill =====")
        total = 0
        for item, qty in self.orders.items():
            # Find price from menu
            for items in self.menu.values():
                if item in items:
                    item_total = items[item] * qty
                    break
            total += item_total
            print(item,"*",qty,"=",item_total)
        print("\nTotal Amount:",total)


# Program Execution
MCS = MenuCardSystem()
MCS.display_menu()
MCS.take_order()
MCS.display_bill()
