# accepts user input in MM/DD/YYYY
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
# output same date in YYYY/MM/DD
while True:
    try:
        date = input("Date: ")
        if date[0].isdigit():
            m, d, y = date.split("/")
            if 1 <= int(m) <= 12 and 1 <= int(d) <= 31:
                print(y + "-" + m.zfill(2) + "-" + d.zfill(2))
                break

        elif date[0].isalpha():
            m, d, y = date.split(" ")
            # remove comma from d variable
            d = d.replace(",", "")
            if m in months:
                m = months.index(m) + 1
                if 1 <= int(m) <= 12 and 1 <= int(d) <= 31:
                    print(y + "-" + f"{m:02}" + "-" + d.zfill(2))
                    break

    except ValueError:
        pass

# if user input is not valid then prompt again
