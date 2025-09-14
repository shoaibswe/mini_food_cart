#rastourant menu
from collections import Counter


menue ={
    "burger": 5.99,
    "fries": 2.99,
    "soda": 1.49,
    "salad": 4.49,
    "ice cream": 3.49
}


def display_menu():
    print("---- Menu: ----")
    # for item, price in menue.items():
    #     print(f"{item},${price}")
    for index, (item, price) in enumerate(menue.items(), 1):
        print(f"{index}. {item},${price}")
    print("---------------")


def take_order():
    order_list =[]
    print("Enter item name or number or 'q' to exit")
    while True:
        item = input().lower()
        # Check if input is a number (menu index)
        if item.isdigit():
            index = int(item) - 1
            menu_items = list(menue.keys())
            if 0 <= index < len(menu_items):
                item = menu_items[index]
        if item == 'q':
            break
        elif menue.get(item) is None:
            print("! Item not found. Please try again.")
        elif item in menue:
            order_list.append(item)
            print(f"{item.title()} : {menue.get(item,0)} added to your order.")
            # print(f"Total : {sum(menue.get(item,0) for item in order_list)}")
            print("Add more item or 'q' to exit")
        else:
            print("! Something went wrong. Please try again.")
    return order_list


def calculate_subtotal(order_list):
    item_count = Counter(order_list)
    print("==== Your Order: ====")
    # print(item_count):  Counter({'salad': 2, 'fries': 3, 'burger': 1})
    for item, quantity in item_count.items():
        price = menue.get(item,0)
        subtotal = price * quantity
        print(f"- {item.title()}, {quantity}pc : ${subtotal:.2f}")
    return item_count


def calculate_total(item_count):
    total = 0.0
    # for item, quantity in item_count.items():
    #     price = menue.get(item,0)
    #     subtotal = price * quantity
    #     total += subtotal
    total = sum(menue.get(item,0) * quantity for item, quantity in item_count.items())
    return total


def main():
        
        display_menu()

        total_amount = \
            calculate_total( \
            calculate_subtotal( \
                take_order()
                ))
        print("--------------------")
        print(f"Total amount: ${total_amount:.2f}")
        print("====================")
        print("Thank you for your order!")


if __name__ == "__main__":
    main()

