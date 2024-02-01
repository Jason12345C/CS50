# grocery.py

# Initialize an empty dictionary to store the items and their counts
grocery_list = {}

# Read the items from standard input, one per line
while True:
    try:
        item = input()
        # Increment the count for the item in the dictionary
        if item.lower() in grocery_list:
            grocery_list[item.lower()] += 1
        else:
            grocery_list[item.lower()] = 1
    except EOFError:
        # End the loop when control-d is pressed
        break

# Print the grocery list in all uppercase, sorted alphabetically
for item in sorted(grocery_list.keys()):
    print(f"{grocery_list[item]} {item.upper()}")
