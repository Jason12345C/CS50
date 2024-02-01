import sys

count = 0

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

try:
    with open(sys.argv[1], "r") as file:
        for line in file: 
            if line.isspace():
                pass
            elif line.strip().startswith("#"):
                pass
            else:
                count += 1

except IndexError:
    sys.exit("Too few command-line arguments")

except FileNotFoundError:
    sys.exit("File does not exist")

print(count)
