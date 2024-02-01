#def main function
#ask user to input face
#convert the face using function
def main():
    msg = input()
    result = convert(msg)
    print(result)

#defne convert
#replace :) with happy emoticon
#replace :( with sad emoticon
def convert(face):
    happyface = face.replace(":)","🙂")
    sadface = happyface.replace(":(","🙁")
    return sadface

#call main
main()