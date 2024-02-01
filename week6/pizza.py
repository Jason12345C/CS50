import sys
import csv
from tabulate import tabulate

items = []

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

try:
    with open(sys.argv[1], "r") as file:
        pizza_items = csv.DictReader(file)
        for line in pizza_items:
            items.append(line)

except FileNotFoundError:
    sys.exit("File does not exist")

except IndexError:
    sys.exit("Too few command-line arguments")

if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")


print(tabulate(items, headers="keys", tablefmt="grid"))
    