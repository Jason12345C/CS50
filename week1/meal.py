def main():
    time = input("What time is it? ")
    time = convert(time)
    if 7.0 <= time <= 8.0:
        print("breakfast time")

    elif 12.0 <= time <= 13.0:
        print("lunch time")

    elif 18.0 <= time <= 19.0:
        print("dinner time")


def convert(time):
    (hour, minute) = time.split(":")
    result = (float(hour) + (float(minute)/60))
    return result


if __name__ == "__main__":
    main()
