# coke = 50 cents, prompt user to insert a coin, one at a time
amount_due = 50

while amount_due > 0:
    print("Amount Due: " + str(amount_due))
    insert_coin = int(input("Insert Coin: "))

    if insert_coin in [5, 10, 25]:
        amount_due -= insert_coin
    # after each insert, inform the user the amount due
    # when the coin inserted is at least 50 cents, output the changed user is owed

if amount_due <= 0:
    print("Change Owed: " + str(abs(amount_due)))


