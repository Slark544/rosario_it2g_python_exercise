# ==========================================
# RECEIPT MODULE
# ==========================================

class Receipt:
    def __init__(self, order):
        self.order = order

    # ---------- PRINT RECEIPT ----------
    def print_receipt(self):
        subtotal = self.order.calculate_subtotal()
        discount = self.order.calculate_discount()
        total = self.order.calculate_total()

        print("\n")
        print("=" * 65)
        print("                    ROSARIO FAST FOOD")
        print("                     OFFICIAL RECEIPT")
        print("=" * 65)

        print(
            f"{'ITEM':<25}"
            f"{'QTY':>5}"
            f"{'PRICE':>15}"
            f"{'TOTAL':>15}"
        )

        print("-" * 65)

        for item in self.order.orders.values():
            item_total = item["price"] * item["quantity"]

            print(
                f"{item['name']:<25}"
                f"{item['quantity']:>5}"
                f"₱{item['price']:>14.2f}"
                f"₱{item_total:>14.2f}"
            )

        print("-" * 65)

        print(
            f"{'SUBTOTAL':<45}"
            f"₱{subtotal:>14.2f}"
        )

        print(
            f"{'DISCOUNT':<45}"
            f"₱{discount:>14.2f}"
        )

        print("=" * 65)

        print(
            f"{'TOTAL AMOUNT':<45}"
            f"₱{total:>14.2f}"
        )

        print("=" * 65)

        if discount > 0:
            print(
                "          Congratulations!"
            )
            print(
                "          You received a 10% discount."
            )

        print("             Thank you for ordering!")
        print("              Please come again!")
        print("=" * 65)
