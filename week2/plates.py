def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # 2-6 characters (letters or numbers)
    if len(s) < 2 or len(s) > 6:
        return False
    # plate start with at least two letters
    elif not s[0:2].isalpha():
        return False

    # no number in the middle of the plate, must come at the end
    for char in range(len(s)):
        if s[char].isdigit():
            if not s[char:].isdigit():
                return False
    # first number cannot be 0
    char = 0
    while char < len(s):
        if not s[char].isalpha():
            if s[char] == "0":
                if s[char:].isdigit():
                    return False
            else:
                break
        char += 1

    # No periods, spaces, or punctuation marks are allowed
    for char in s:
        if char.isalnum() is False:
            return False

    return True

if __name__ == "__main__":
    main()
