import random

# if incorrect, print EEE and prompt again, up to 3 times
# if incorrect after 3 tries, output correct answer
# output user score out of 10


def main():
    n = get_level()
    i = 1  # question count
    j = 1  # mistakes count
    score = 0  # score count
    while i <= 10:
        x = generate_integer(n)
        y = generate_integer(n)
        answer = int(input(f"{x}+{y}= "))
        if answer == (x+y):
            score += 1
        elif answer != (x + y):
            while j <= 2:
                print("EEE")
                answer = int(input(f"{x}+{y}= "))
                if answer == (x+y):
                    score += 1
                    break
            j += 1
        i += 1
    print(f"score:{score}")


def get_level():  # prompt user for level, if user does not input 1,2,or 3, prompt again
    while True:
        try:
            level = int(input("level: "))
            if not 1 <= level <= 3:
                int(input("level: "))
            else:
                return level
        except ValueError:
            pass


def generate_integer(level):
    # randomly generate x, y
    # X and Y should be non-negative, with n digits
    if level == 1:
        random_x = random.randint(1, 9)
        random_y = random.randint(1, 9)
        return random_x and random_y
    elif level == 2:
        random_x = random.randint(10, 99)
        random_y = random.randint(10, 99)
        return random_x and random_y
    elif level == 3:
        random_x = random.randint(100, 999)
        random_y = random.randint(100, 999)
        return random_x and random_y


if __name__ == "__main__":
    main()
