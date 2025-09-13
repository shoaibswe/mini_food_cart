#mini food cart

menue = {
    "burger": 5.99,
    "fries": 2.99,
    "soda": 1.49,
    "salad": 4.49,
    "ice cream": 3.49
}
order = []
total = 0.0

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
            print(f"{item.title()} added to your order.")
            # total += menue[item]
        else:
            print("Something went wrong. Please try again.")

def calculate_total():
    # print(f"Total amount due: ${total:.2f}")
    global total
    for item in order:
        total += menue[item]
    print(f"Total amount due: ${total:.2f}")

def main():
    display_menu()
    take_order()
    calculate_total()
    print("Thank you for your order!")

if __name__ == "__main__":
    main()
