# ==========================================
# ORDER MODULE
# ==========================================

class Order:
    def __init__(self):
        self.orders = {}

    # ---------- GET QUANTITY ----------
    def get_quantity(self):
        while True:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    return quantity

                print("Quantity must be greater than zero.")

            except ValueError:
                print("Invalid quantity. Please enter a whole number.")

    # ---------- ADD ORDER ----------
    def add_order(self, menu):
        item_number = menu.get_item()
        quantity = self.get_quantity()

        item = menu.get_item_info(item_number)

        if item_number in self.orders:
            self.orders[item_number]["quantity"] += quantity
        else:
            self.orders[item_number] = {
                "name": item["name"],
                "price": item["price"],
                "quantity": quantity
            }

        print(
            f"\nAdded {quantity} x {item['name']} "
            "to your order."
        )

    # ---------- CALCULATE SUBTOTAL ----------
    def calculate_subtotal(self):
        subtotal = 0

        for item in self.orders.values():
            subtotal += item["price"] * item["quantity"]

        return subtotal

    # ---------- CALCULATE DISCOUNT ----------
    def calculate_discount(self):
        subtotal = self.calculate_subtotal()

        if subtotal >= 500:
            return subtotal * 0.10

        return 0

    # ---------- CALCULATE TOTAL ----------
    def calculate_total(self):
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()

        return subtotal - discount
