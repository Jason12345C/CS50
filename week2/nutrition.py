item = input("Item: ").strip().lower()

fruit = {"apple": "130", "avocado": "50", "banana": "110", "cantaloupe": "50",
         "grapefruit": "60", "grapes": "90", "honeydew melon": "50", "kiwifruit": "90",
         "lemon": "15", "lime": "20", "orange": "80", "peach": "60", "pear": "100",
         "pineapple": "50", "plums": "70", "strawberries": "50", "sweet cherries": "100",
         "tangerine": "50", "watermelon": "80"}

while True:
    if item not in fruit:
        item = input("Item: ").strip().lower()

    else:
        if item in fruit:
            print(fruit[item])
        break









