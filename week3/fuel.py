while True:
    try:
        # prompt user for a fraction, formatted as X/Y
        fraction1 = input("Enter fraction: ")
        x, y = fraction1.split("/")
        fraction2 = int(x) / int(y)
        if fraction2 <= 1:
            break
        elif fraction2 > 1:
            print("Fraction should be between 0 and 1")
    # if x or y is not an integer, x > y, or y = 0, prompt user again
    except ValueError:
        print("Please enter a fraction between 0 and 1")
    except ZeroDivisionError:
        print("Fraction Cannot Be Divided By Zero")

# output percentage rounded to the nearest integer amount of fuel left

new_fraction = round(fraction2 * 100)

# if 1% or less remains, output E
if 0 <= new_fraction <= 1:
    print("E")
# if 99% or more remains, output F
elif 99 <= new_fraction <= 100:
    print("F")
else:
    print(new_fraction, "%", sep="")
