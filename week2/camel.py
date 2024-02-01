def main():
    camelcase = input("Enter name of a variable in camel case: ").strip()
    print("snake_case:", end=" ")
    snake_case(camelcase)


def snake_case(var):
    for letter in var:
        if letter.isupper():
            print("_" + letter.lower(), end="")

        else:
            print(letter, end="")


main()
