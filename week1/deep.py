#ask user for answer to question
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

#take away - from answer, remove spaces and make it all lower case
answer = answer.replace("-"," ").strip().lower()

# match case, if 42 or its equivalent, then yes, otherwise no.
match answer:
    case "forty two"| "42":
        print("Yes")
    case _:
        print("No")

