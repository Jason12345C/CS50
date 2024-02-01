# prompt user to input expression
expression = input("Expression: ")

# split the str expression into x, y, and z. x is the first number, y is the math operator,
# and z is the second number
[x, y, z] = expression.split(sep=" ")

if y == "+":
    ans = float(x) + float(z)
    print(f"{ans:.1f}")

elif y == "-":
    ans = float(x) - float(z)
    print(f"{ans:.1f}")

elif y == "*":
    ans = float(x) * float(z)
    print(f"{ans:.1f}")

elif y == "/":
    ans = float(x) / float(z)
    print(f"{ans:.1f}")

else:
    print("expression is invalid")

