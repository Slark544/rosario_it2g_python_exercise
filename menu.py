# ==========================================
# MENU MODULE
# ==========================================

class Menu:
    def __init__(self):
        self.items = {
            "1": {"name": "Chicken Burger", "price": 85.00},
            "2": {"name": "Cheese Burger", "price": 95.00},
            "3": {"name": "French Fries", "price": 55.00},
            "4": {"name": "Chicken Nuggets", "price": 75.00},
            "5": {"name": "Spaghetti", "price": 80.00},
            "6": {"name": "Iced Tea", "price": 40.00},
            "7": {"name": "Soft Drink", "price": 45.00},
            "8": {"name": "Chocolate Sundae", "price": 50.00}
        }

    # ---------- DISPLAY MENU ----------
    def display_menu(self):
        print("\n" + "=" * 50)
        print("          ROSARIO FAST FOOD")
        print("=" * 50)
        print("                    MENU")
        print("-" * 50)

        for number, item in self.items.items():
            print(
                f"{number}. {item['name']:<25}"
                f"₱{item['price']:>7.2f}"
            )

        print("-" * 50)

    # ---------- GET MENU ITEM ----------
    def get_item(self):
        while True:
            choice = input("Enter the menu number: ").strip()

            if choice in self.items:
                return choice

            print("Invalid menu number. Please try again.")

    # ---------- GET ITEM INFORMATION ----------
    def get_item_info(self, item_number):
        return self.items[item_number]
