for _ in range(3):
    name = input("Enter name: ")
    print(name)
    with open("names.txt", "a") as f:
        f.write(f"{name}\n")
