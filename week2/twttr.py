def main():
    text = input("Type word: ").strip()
    print(shorten(text))


def shorten(txt):
    # ask user for input
    vowels_lower = ["a", "e", "i", "o", "u"]
    # go through each letter and delete if it is a vowel
    word_no_vowels = ""
    for letter in txt:
        if not letter.lower() in vowels_lower:
            # return
            word_no_vowels += letter
    return word_no_vowels.strip()


if __name__ == "__main__":
    main()
