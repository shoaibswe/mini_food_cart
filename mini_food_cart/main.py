#mini food cart
from collections import Counter

menue = {
    "burger": 5.99,
    "fries": 2.99,
    "soda": 1.49,
    "salad": 4.49,
    "ice cream": 3.49
}

order = []
total = 0.0
items_count = Counter()

def display_menu():
    print("---- Menu: ----")
    for item, price in menue.items():
        print(f"{item}: ${price:.2f}")

def take_order():
    while True:
        item = input("Enter an item to order (or 'done' or 'q' to finish): ").lower()
        if item == 'done' or item == 'q':
            break
        elif menue.get(item) is None:
            print("Item not found. Please try again.")
        elif item in menue:
            order.append(item)
            print(f"{item.title()}, ${menue.get(item,0)} added to your order.")
        else:
            print("Something went wrong. Please try again.")

def calculate_total():
    for item in order:
        global total
        total += menue.get(item, 0)
    print(f"Total amount: ${total:.2f}")

def show_order():
    print("--- Your Order: ---")
    items_count = Counter(order)
    # print(items_count)
    for item, quantity in items_count.items():
        price = menue.get(item, 0)
        subtotal = price * quantity
        print(f"- {item.title()}")
        print(f"  Price: ${price:.2f}")
        print(f"  Quantity: {quantity}")
        print(f"  Subtotal: ${subtotal:.2f}")

def main():
    display_menu()
    take_order()
    show_order()
    print("------------------")
    calculate_total()
    print("------------------")
    print("Thank you for your order!")

if __name__ == "__main__":
    main()
