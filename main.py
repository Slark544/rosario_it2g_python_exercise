# ==========================================
# ROSARIO FAST FOOD ORDERING SYSTEM
# MAIN MODULE
# ==========================================

from menu import Menu
from order import Order
from receipt import Receipt


# ---------- GET YES OR NO ----------
def get_yes_no(question):
    while True:
        answer = input(question).strip().lower()

        if answer == "yes" or answer == "y":
            return True

        elif answer == "no" or answer == "n":
            return False

        else:
            print(
                "Invalid input. "
                "Please enter Yes or No."
            )


# ---------- MAIN PROGRAM ----------
def main():

    menu = Menu()
    order = Order()

    print("\n" + "=" * 50)
    print("       WELCOME TO ROSARIO FAST FOOD")
    print("=" * 50)

    menu.display_menu()

    wants_to_order = get_yes_no(
        "\nWould you like to place an order? (Yes/No): "
    )

    if not wants_to_order:
        print(
            "\nThank you for visiting "
            "Rosario Fast Food!"
        )
        print("Have a great day!")
        return

    # ---------- FIRST ORDER ----------
    order.add_order(menu)

    # ---------- ADDITIONAL ORDERS ----------
    while get_yes_no(
        "\nWould you like to order another item? (Yes/No): "
    ):
        order.add_order(menu)

    # ---------- PRINT RECEIPT ----------
    receipt = Receipt(order)
    receipt.print_receipt()


# ---------- PROGRAM START ----------
if __name__ == "__main__":
    main()
