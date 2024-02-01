# prompt user for a level, n
# if user does not input positive int, prompt again
while True:
    try:
        n = int(input("Level: "))
        if n <= 0:
            n = int(input("Guess: "))
        if n > 0:
            break
    except ValueError:
        pass

# randomly generates an int between 1 and n, inclusively
from random import randint
random_n = randint(1, n)

# prompt to guess int
# if guess != positive int, prompt again
while True:
    try:
        Guess = int(input("Guess: "))
        if Guess <= 0:
            Guess = int(input("Guess: "))
        else:
            break
    except ValueError:
        pass

# if guess < int, print too small
while True:
    if 0 < Guess < random_n:
        print("Too small!")
        Guess = int(input("Guess: "))
    # if guess > int, print too large
    elif 0 < Guess and Guess > random_n:
        print("Too large!")
        Guess = int(input("Guess: "))
    else:
        break

# if guess = int, print just right, and exit
print("Just right!")
