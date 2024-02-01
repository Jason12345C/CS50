def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# dollar to float accepts str (ex: $10.00) and returns a float
#remove dollar sign
#convert to float
def dollars_to_float(d):
    d = d.strip("$")
    dollars = float(d)
    return dollars

# percent to float accepts a str (ex: 15%) and returns a float
#remove percent sign
#convert to float
def percent_to_float(p):
    percent = p.strip("%")
    p = float(percent)
    finalp = p/100
    return finalp

main()
