def main():
    # prompt user for input
    # remove whitespace and input is case-insensitive
    greet = input("Enter greeting: ").strip()
    print(value(greet))

def value(greeting):
    # if greeting is hello, then print $0
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        return "0"

    # if greeting begins with h, then print $20
    elif greeting.startswith("h"):
        return "20"

    # otherwise, print $100
    else:
        return "100"


if __name__ == "__main__":
    main()
    