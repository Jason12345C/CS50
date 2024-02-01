menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }

total = 0
while True:
    try:
        # prompt user to order
        item = input("Item: ").strip().lower().title()
        if item in menu:
            # after each inputted item, display the total cost of all items
            total += menu[item]
            # prefix total with dollar sign, formatted to two decimal places
            print(f"${total:.2f}")
    except EOFError:
        break

# ignore any input that isn't an item
# assume input is title cased
