# prompt user for name until control-d,
# assume user inputs at least one name
# loop forever with while loop
import inflect

p = inflect.engine()

list_of_names = []

while True:
    try:
        name = input("Name: ")
        list_of_names.append(name)
    except EOFError:
        break

# separate two names with "and"
# separate three names with two commas and one "and"
# n names with n-1 commas and one and one "and"
print("\n", end="")
print("Adieu, adieu, to " + p.join(list_of_names))
