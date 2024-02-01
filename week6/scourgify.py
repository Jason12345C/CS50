import sys
import csv

first = []
last = []
house = []
with open(sys.argv[1], "r") as readingfile:
    reader = csv.DictReader(readingfile)
    for row in reader:
        last_name,first_name = (row["name"].split(","))
        first.append(first_name)
        last.append(last_name)
        house.append(row["house"])

with open(sys.argv[2], "a") as writingfile:
    for first in first:
        writer = csv.DictWriter(writingfile, fieldnames = "first")
        writer.writerow({"first": first})
